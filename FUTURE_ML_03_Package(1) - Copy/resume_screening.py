import os
import pandas as pd
import matplotlib.pyplot as plt

from utils import (
    extract_text,
    calculate_similarity,
    extract_skills,
    extract_name,
    extract_email,
    extract_phone
)

# -------------------------------
# Paths
# -------------------------------

RESUME_FOLDER = "dataset/resumes"
JOB_DESCRIPTION_FILE = "dataset/job_description.txt"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# -------------------------------
# Read Job Description
# -------------------------------

with open(JOB_DESCRIPTION_FILE, "r", encoding="utf-8") as file:
    job_description = file.read()

results = []

# -------------------------------
# Process Each Resume
# -------------------------------

for file in os.listdir(RESUME_FOLDER):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(RESUME_FOLDER, file)

        print(f"Processing: {file}")

        # Extract resume text
        resume_text = extract_text(pdf_path)

        # Debug (optional)
        print("\n" + "=" * 60)
        print(f"Extracted text from: {file}")
        print("=" * 60)
        print(resume_text[:1000])
        print("=" * 60 + "\n")

        # Candidate Details
        candidate_name = extract_name(resume_text)
        candidate_email = extract_email(resume_text)
        candidate_phone = extract_phone(resume_text)

        # ATS Score
        ats_score = calculate_similarity(
            job_description,
            resume_text
        )

        # Skills
        matched_skills, missing_skills = extract_skills(
            resume_text
        )

        # Store Result
        results.append({
            "Candidate": candidate_name,
            "Email": candidate_email,
            "Phone": candidate_phone,
            "Resume File": file,
            "ATS Score": ats_score,
            "Matched Skills": ", ".join(matched_skills),
            "Missing Skills": ", ".join(missing_skills)
        })

# -------------------------------
# Create DataFrame
# -------------------------------

df = pd.DataFrame(results)

df = df.sort_values(
    by="ATS Score",
    ascending=False
).reset_index(drop=True)

df.insert(
    0,
    "Rank",
    range(1, len(df) + 1)
)

# -------------------------------
# Save CSV
# -------------------------------

csv_path = os.path.join(
    OUTPUT_FOLDER,
    "ranked_candidates.csv"
)

df.to_csv(csv_path, index=False)

# -------------------------------
# Plot Graph
# -------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    df["Candidate"],
    df["ATS Score"]
)

plt.title("ATS Resume Ranking")

plt.xlabel("Candidate")

plt.ylabel("ATS Score")

plt.xticks(rotation=20)

plt.tight_layout()

graph_path = os.path.join(
    OUTPUT_FOLDER,
    "candidate_ranking.png"
)

plt.savefig(graph_path)

plt.close()

# -------------------------------
# Display Results
# -------------------------------

print("\n========== ATS Resume Ranking ==========\n")

print(df[[
    "Rank",
    "Candidate",
    "Email",
    "Phone",
    "ATS Score"
]])

print("\nCSV Saved:", csv_path)
print("Graph Saved:", graph_path)

print("\nProject Completed Successfully!")