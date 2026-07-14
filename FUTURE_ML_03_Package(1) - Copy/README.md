# Future Interns Task 3
# 📄 AI-Powered ATS Resume Screening System

## 📌 Overview

AI-Powered ATS Resume Screening System is a machine learning-based application that analyzes resumes against job descriptions and ranks candidates based on ATS compatibility score.

The system uses NLP-based skill matching to identify candidate strengths, missing skills, and provides resume improvement suggestions.

---

# ✨ Features

## 📄 Resume Parsing
- Upload resume PDF files
- Extract candidate information
- Extract technical skills automatically

## 🎯 ATS Score Calculation
- Compare resume with job description
- Calculate compatibility score
- Identify matched and missing skills

## 🏆 Candidate Ranking
- Rank candidates based on ATS score
- Display top matching candidates
- Generate candidate reports

## 📊 Dashboard
- Total candidates
- Highest ATS score
- Average ATS score
- Candidate ranking table
- Skill analysis

## 🤖 AI Resume Feedback
- Shows strong skills
- Highlights missing skills
- Provides improvement suggestions

---

# 🏗️ Project Workflow

```
Resume PDF
     |
     ↓
Text Extraction
     |
     ↓
Resume Information Parsing
     |
     ↓
Skill Matching
     |
     ↓
ATS Score Calculation
     |
     ↓
Candidate Ranking
     |
     ↓
Resume Feedback
```

---

# 🛠️ Technologies Used

### Programming Language
- Python

### Framework
- Streamlit

### Libraries
- Pandas
- Plotly
- PyMuPDF
- Scikit-learn

### Concepts
- Natural Language Processing
- Text Extraction
- Skill Matching
- Data Visualization

---

# 📂 Project Structure

```
FUTURE_ML_03

│
├── app.py
├── ats_engine.py
├── parser.py
├── resume_feedback.py
├── resume_preview.py
│
├── requirements.txt
│
└── output
    └── ranked_candidates.csv
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Gayathri-kakumanu/FUTURE_ML_03.git
```

Go inside the project:

```bash
cd FUTURE_ML_03
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

Run:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

# 🖥️ Application Modules

### Dashboard
- Candidate overview
- ATS score statistics
- Ranking information

### Upload Resume
- Upload PDF resume
- Add job description
- Analyze candidate

### Analytics
- ATS score visualization

### Reports
- Download candidate analysis report

---

# 📊 Example Output

```
Candidate:
MANIKANTAN P

ATS Score:
50%

Matched Skills:
Python
Machine Learning
SQL

Missing Skills:
Deep Learning
Pandas
NumPy
Scikit-learn
TensorFlow
NLP
Streamlit
```

---

# 🚀 Future Improvements

- LLM-based resume improvement
- AI-generated resume rewriting
- Multiple job matching
- Cloud deployment
- Database integration
- Advanced NLP models

---

# 👩‍💻 Author

**Gayathri Kakumanu**

B.Tech Computer Science Engineering  
Artificial Intelligence & Machine Learning

GitHub:
https://github.com/Gayathri-kakumanu