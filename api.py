from fastapi import FastAPI
from sqlalchemy.orm import Session
from backend.db import SessionLocal
from backend.models import Submission
from backend.schemas import SubmissionCreate
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/submissions")
def get_submissions():
    db: Session = SessionLocal()
    results = db.query(Submission).all()
    return [s.__dict__ for s in results]

@app.post("/submission")
def post_submission(sub: SubmissionCreate):
    db: Session = SessionLocal()
    new_sub = Submission(
        username=sub.username,
        problem_slug=sub.problem_slug,
        source_code=sub.source_code,
        srclink=sub.srclink,
        timestamp = sub.timestamp
    )
    db.add(new_sub)
    db.commit()
    return {"message": "Inserted"}
