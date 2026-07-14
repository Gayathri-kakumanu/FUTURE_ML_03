import fitz
import re

SKILLS = [
    "python","java","c","c++","sql","mysql","postgresql",
    "html","css","javascript","react","node","express",
    "machine learning","deep learning","tensorflow","keras",
    "pytorch","scikit-learn","pandas","numpy","matplotlib",
    "power bi","tableau","excel","git","github",
    "docker","aws","azure","flask","django"
]


def extract_text(pdf):
    text = ""

    doc = fitz.open(stream=pdf.read(), filetype="pdf")

    for page in doc:
        text += page.get_text()

    return text


def extract_email(text):
    email = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return email.group(0) if email else "Not Found"


def extract_phone(text):
    phone = re.search(r'(\+?\d[\d\s\-]{8,}\d)', text)
    return phone.group(0) if phone else "Not Found"


def extract_name(text):
    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if (
            len(line.split()) <= 4
            and len(line) > 2
            and "resume" not in line.lower()
            and "curriculum" not in line.lower()
        ):
            return line

    return "Unknown"


def extract_skills(text):

    skills_list = [

        "Python",
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "AI",
        "ML",
        "SQL",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch",
        "NLP",
        "Natural Language Processing",
        "Data Analysis",
        "Streamlit",
        "Power BI",
        "Tableau",
        "AWS",
        "Cloud Computing",
        "Docker",
        "Git",
        "GitHub"

    ]


    extracted = []


    text = text.lower()


    for skill in skills_list:

        if skill.lower() in text:

            extracted.append(skill)


    return extracted