# Code Plagiarism Checker

A full-stack application that detects plagiarism in coding contest submissions using TF-IDF and cosine similarity. It includes a REST API (FastAPI) backend and an interactive Streamlit frontend.

---

## 🛠️ Features

- 📁 Dual-mode: Upload code files or simulate contest data.
- 📊 TF-IDF + Cosine Similarity for code comparison.
- 🔥 Heatmap and matrix view of similarity scores.
- 🚨 Plagiarism detection with adjustable similarity threshold.
- 🧠 Backend in FastAPI, frontend in Streamlit.
- 🗃️ MySQL database for persistent code submissions.

---

## 🧩 Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Database**: MySQL (via SQLAlchemy)
- **ML**: TF-IDF Vectorizer + Cosine Similarity
- **Others**: Seaborn, Matplotlib, Pandas, Scikit-learn

---

## 📂 Project Structure

project-root/
│
├── backend/
│ ├── api.py # FastAPI endpoints
│ ├── db.py # Database connection
│ ├── models.py # SQLAlchemy ORM models
│ ├── schemas.py # Pydantic schemas
│
├── frontend/
│ └── app.py # Streamlit app
│
├── test/
│ ├── code.py # Sample user submission 1
│ ├── code2.py # Sample user submission 2
│ ├── code.java # Sample Java code
│ └── test.py # FastAPI test route
│
├── database/
│ └── init_db.sql # SQL schema for 'submissions' table
│
├── README.md
└── requirements.txt 


---

## 🚀 How to Run the Project

### 1. 🧰 Set Up MySQL

```sql
# In MySQL console
source database/init_db.sql;
2. ⚙️ Backend - FastAPI
bash
Copy
Edit
cd backend/
uvicorn api:app --reload
Runs at: http://127.0.0.1:8000

3. 🎛️ Frontend - Streamlit
bash
Copy
Edit
cd frontend/
streamlit run app.py
Opens in browser: http://localhost:8501

🌐 API Endpoints
Method	Endpoint	Description
GET	/submissions	Fetch all code entries
POST	/submission	Submit new code metadata

🧪 Sample Submissions Format
json
Copy
Edit
{
  "username": "john_doe",
  "problem_slug": "sum-integers",
  "source_code": "print(sum(map(int, input().split())))",
  "srclink": "http://example.com/code.py",
  "timestamp": "2024-05-01T12:00:00"
}
🎯 Future Enhancements
Code syntax normalization before comparison

Integration with GitHub/GitLab for submission pulls

Admin dashboard for contest insights

Code similarity visualization with AST

