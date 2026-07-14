from resume_feedback import generate_feedback

import plotly.express as px
import os
import pandas as pd
import streamlit as st

from streamlit_option_menu import option_menu

from parser import (
    extract_text,
    extract_name,
    extract_email,
    extract_phone,
    extract_skills
)

from ats_engine import calculate_ats_score



# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI ATS Resume Screening System",
    page_icon="📄",
    layout="wide"
)



# =========================
# SIDEBAR
# =========================

with st.sidebar:

    selected = option_menu(

        "ATS Resume Screening",

        [
            "Dashboard",
            "Upload Resumes",
            "Analytics",
            "Reports"
        ],

        icons=[
            "speedometer2",
            "cloud-upload",
            "bar-chart",
            "file-earmark-text"
        ],

        menu_icon="robot",

        default_index=0
    )



# =========================
# HEADER
# =========================

st.title(
    "📄 AI-Powered ATS Resume Screening System"
)

st.caption(
    "Resume Analysis | Candidate Ranking | Skill Matching"
)



# =====================================================
# DASHBOARD
# =====================================================

if selected == "Dashboard":


    st.header("📊 Dashboard")


    path = "output/ranked_candidates.csv"



    if os.path.exists(path):


        try:

            df = pd.read_csv(path)


        except pd.errors.EmptyDataError:

            st.warning(
                "No resume analysis found."
            )

            st.stop()



        if df.empty:

            st.warning(
                "No candidate data available."
            )

            st.stop()



        df["ATS Score"] = pd.to_numeric(

            df["ATS Score"],

            errors="coerce"

        ).fillna(0)



        df = df.sort_values(

            "ATS Score",

            ascending=False

        )



        df.insert(

            0,

            "Rank",

            range(1,len(df)+1)

        )



        def status(score):

            if score >= 80:

                return "🟢 Excellent Match"

            elif score >= 60:

                return "🟡 Good Match"

            else:

                return "🔴 Needs Improvement"



        df["Status"] = df["ATS Score"].apply(status)



        c1,c2,c3,c4 = st.columns(4)


        c1.metric(
            "Total Candidates",
            len(df)
        )


        c2.metric(
            "Highest Score",
            f"{df['ATS Score'].max():.2f}%"
        )


        c3.metric(
            "Average Score",
            f"{df['ATS Score'].mean():.2f}%"
        )


        c4.metric(
            "Excellent Matches",
            len(df[df["ATS Score"]>=80])
        )



        st.divider()



        st.subheader(
            "🏆 Candidate Ranking"
        )


        st.dataframe(

            df,

            use_container_width=True

        )



        # Top candidate

        top = df.iloc[0]



        st.subheader(
            "🥇 Top Candidate Analysis"
        )



        col1,col2 = st.columns(2)



        with col1:

            st.metric(
                "Candidate",
                top["Name"]
            )


            st.metric(
                "ATS Score",
                f"{top['ATS Score']:.2f}%"
            )


            st.write(
                "Status:",
                top["Status"]
            )



        with col2:

            st.write(
                "📧 Email:",
                top["Email"]
            )


            st.write(
                "📱 Phone:",
                top["Phone"]
            )



        # Skills

        st.subheader(
            "🛠 Skills Analysis"
        )


        col3,col4 = st.columns(2)



        with col3:

            st.success(
                "✅ Matched Skills"
            )

            st.write(
                top["Matched Skills"]
            )



        with col4:

            st.error(
                "❌ Missing Skills"
            )

            st.write(
                top["Missing Skills"]
            )



        # =========================
        # AI FEEDBACK
        # =========================

        st.subheader(
            "🤖 AI Resume Feedback"
        )


        matched = [

            x.strip()

            for x in str(top["Matched Skills"]).split(",")

        ]



        missing = [

            x.strip()

            for x in str(top["Missing Skills"]).split(",")

        ]



        feedback = generate_feedback(

            top["ATS Score"],

            matched,

            missing

        )



        for item in feedback:

            st.info(item)



    else:


        st.info(
            "Upload resumes and analyze first."
        )





# =====================================================
# UPLOAD RESUMES
# =====================================================

elif selected == "Upload Resumes":


    st.header(
        "📤 Upload Resumes"
    )


    job_description = st.text_area(

        "📌 Paste Job Description",

        height=220

    )



    uploaded_files = st.file_uploader(

        "Upload Resume PDFs",

        type="pdf",

        accept_multiple_files=True

    )



    if uploaded_files and job_description:


        if st.button(
            "🚀 Analyze Resumes"
        ):


            results=[]



            for file in uploaded_files:


                text = extract_text(file)



                name = extract_name(text)

                email = extract_email(text)

                phone = extract_phone(text)

                skills = extract_skills(text)



                score,matched,missing = calculate_ats_score(

                    text,

                    job_description

                )



                results.append({

                    "Name":name,

                    "Email":email,

                    "Phone":phone,

                    "Skills":", ".join(skills),

                    "ATS Score":score,

                    "Matched Skills":", ".join(matched),

                    "Missing Skills":", ".join(missing)

                })



            result = pd.DataFrame(results)



            os.makedirs(

                "output",

                exist_ok=True

            )



            result.to_csv(

                "output/ranked_candidates.csv",

                index=False

            )



            st.success(
                "✅ Resume analysis completed"
            )



            st.dataframe(

                result,

                use_container_width=True

            )



    elif uploaded_files:


        st.warning(
            "Please add Job Description."
        )





# =====================================================
# ANALYTICS
# =====================================================

elif selected == "Analytics":


    st.header(
        "📈 Analytics"
    )


    if os.path.exists(
        "output/ranked_candidates.csv"
    ):


        data = pd.read_csv(

            "output/ranked_candidates.csv"

        )


        fig = px.bar(

            data,

            x="Name",

            y="ATS Score",

            color="ATS Score",

            title="Candidate ATS Score"

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )


    else:

        st.info(
            "No data available."
        )





# =====================================================
# REPORTS
# =====================================================

elif selected == "Reports":


    st.header(
        "📑 Reports"
    )


    if os.path.exists(

        "output/ranked_candidates.csv"

    ):


        report = pd.read_csv(

            "output/ranked_candidates.csv"

        )


        st.dataframe(

            report,

            use_container_width=True

        )


        st.download_button(

            "📥 Download CSV",

            report.to_csv(index=False),

            "ATS_Report.csv",

            "text/csv"

        )


    else:


        st.warning(
            "No reports available."
        )