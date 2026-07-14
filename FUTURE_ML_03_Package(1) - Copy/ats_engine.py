def calculate_ats_score(resume_text, job_description):

    resume_text = resume_text.lower()
    job_description = job_description.lower()


    # Important AI/ML skills with weights
    skill_weights = {

        "python": 20,

        "machine learning": 20,

        "sql": 10,

        "deep learning": 10,

        "pandas": 10,

        "numpy": 5,

        "scikit-learn": 10,

        "tensorflow": 5,

        "nlp": 5,

        "streamlit": 5

    }


    matched_skills = []

    missing_skills = []

    score = 0



    for skill, weight in skill_weights.items():


        # Check skill in resume

        if skill in resume_text:


            matched_skills.append(skill)

            score += weight



        else:


            missing_skills.append(skill)



    return (

        round(score, 2),

        matched_skills,

        missing_skills

    )