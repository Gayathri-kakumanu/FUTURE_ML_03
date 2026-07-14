# 📄 AI-Powered ATS Resume Screening System

An intelligent Applicant Tracking System (ATS) that analyzes resumes against job descriptions using Natural Language Processing techniques. The system extracts candidate information, matches skills, calculates ATS compatibility scores, ranks candidates, and provides resume improvement feedback.

---

## 🚀 Features

### 📑 Resume Analysis
- Upload resume PDFs
- Extract candidate details automatically
- Extract technical skills from resumes
- Analyze resume content

### 🎯 ATS Scoring
- Compare resumes with job descriptions
- Calculate ATS compatibility score
- Use weighted skill matching algorithm
- Identify strengths and skill gaps

### 🏆 Candidate Ranking
- Rank candidates based on ATS score
- Display highest matching candidates
- Compare multiple resumes

### 📊 Interactive Dashboard
- Total candidate count
- Highest ATS score
- Average score
- Candidate ranking table
- Skill analysis visualization

### 🤖 AI Resume Feedback
- Shows matched skills
- Identifies missing skills
- Provides improvement suggestions

---

# 🏗️ System Architecture

```
Resume PDF
     |
     ↓
PDF Text Extraction
     |
     ↓
Information Extraction
(Name, Email, Phone, Skills)
     |
     ↓
NLP Skill Matching
     |
     ↓
ATS Score Calculation
     |
     ↓
Candidate Ranking
     |
     ↓
AI Resume Feedback
```

---

# 🛠️ Tech Stack

## Programming Language
- Python

## Framework
- Streamlit

## Libraries
- Pandas
- Plotly
- PyMuPDF
- Scikit-learn
- NLP techniques

## Tools
- Git
- GitHub

---

# 📂 Project Structure

```
AI-ATS-Resume-Screening-System

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

Navigate to project folder:

```bash
cd FUTURE_ML_03
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

Start Streamlit:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

# 📌 How It Works

1. Upload one or more resume PDFs.
2. Enter the job description.
3. The system extracts resume information.
4. Skills are matched with job requirements.
5. ATS score is calculated.
6. Candidates are ranked.
7. AI feedback highlights improvement areas.

---

# 📈 Sample Output

Example:

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

# 🎯 Future Enhancements

- Resume improvement generator
- AI-based resume rewriting
- Multiple job matching
- Cloud deployment
- Database integration
- Advanced NLP models
- LLM-powered recruiter assistant

---

# 👩‍💻 Author

**Gayathri Kakumanu**

Computer Science Engineering  
Artificial Intelligence & Machine Learning

GitHub:
https://github.com/Gayathri-kakumanu

---

⭐ If you find this project useful, consider giving it a star!
