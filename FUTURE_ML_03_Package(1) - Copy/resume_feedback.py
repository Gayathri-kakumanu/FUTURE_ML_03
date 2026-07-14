def generate_feedback(score, matched_skills, missing_skills):

    feedback = []


    # Score feedback

    if score >= 80:

        feedback.append(
            "🎯 Excellent match! Resume strongly aligns with the job requirements."
        )

    elif score >= 60:

        feedback.append(
            "👍 Good match. Some additional skills can improve your selection chances."
        )

    else:

        feedback.append(
            "⚠️ Resume needs improvement to better match this job role."
        )



    # Matched skills

    if matched_skills:

        feedback.append(
            "✅ Strong Skills: " +
            ", ".join(matched_skills)
        )



    # Missing skills

    if missing_skills:

        feedback.append(
            "❌ Missing Skills: " +
            ", ".join(missing_skills)
        )



    # Suggestions

    if missing_skills:

        feedback.append(
            "🚀 Recommendation: Add projects, certifications, or hands-on experience related to missing skills."
        )


    return feedback