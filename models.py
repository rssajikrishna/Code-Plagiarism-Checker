from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    problem_slug = Column(String(255))
    source_code = Column(Text)
    srclink = Column(String(500))
    timestamp = Column(DateTime)
