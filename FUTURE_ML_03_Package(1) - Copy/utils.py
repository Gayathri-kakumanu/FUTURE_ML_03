from utils import (
    extract_text,
    calculate_similarity,
    extract_skills,
    extract_name,
    extract_email,
    extract_phone
)
import pdfplumber
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# Skills List
# -------------------------------

SKILLS = [
    "python",
    "sql",
    "machine learning",
    "pandas",
    "numpy",
    "power bi",
    "tableau",
    "excel",
    "flask",
    "git",
    "communication",
    "problem solving"
]

# -------------------------------
# Extract Text from PDF
# -------------------------------

def extract_text(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text.strip()

# -------------------------------
# Clean Text
# -------------------------------

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# -------------------------------
# ATS Score
# -------------------------------

def calculate_similarity(job_description, resume):

    jd = clean_text(job_description)
    resume = clean_text(resume)

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([jd, resume])

    score = cosine_similarity(vectors)[0][1]

    return round(score * 100, 2)

# -------------------------------
# Skill Extraction
# -------------------------------

def extract_skills(resume):

    resume = clean_text(resume)

    matched = []
    missing = []

    for skill in SKILLS:
        if skill in resume:
            matched.append(skill)
        else:
            missing.append(skill)

    return matched, missing

# -------------------------------
# Name Extraction
# -------------------------------

def extract_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if "@" in line:
            continue

        if any(char.isdigit() for char in line):
            continue

        words = line.split()

        # First line with 2–4 words is assumed to be the candidate name
        if 2 <= len(words) <= 4:
            return line

    return "Unknown"

# -------------------------------
# Email Extraction
# -------------------------------

def extract_email(text):

    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return match.group(0) if match else "Not Found"

# -------------------------------
# Phone Extraction
# -------------------------------

def extract_phone(text):

    patterns = [
        r"(\+91[- ]?)?[6-9]\d{9}",
        r"\d{3}[- ]\d{3}[- ]\d{4}",
        r"\(\d{3}\)\s?\d{3}[- ]?\d{4}"
    ]

    for pattern in patterns:
        match = re.search(pattern, text)

        if match:
            return match.group(0)

    return "Not Found"