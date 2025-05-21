from pydantic import BaseModel
from datetime import datetime

class SubmissionCreate(BaseModel):
    username: str
    problem_slug: str
    source_code: str
    srclink: str
    timestamp: datetime
