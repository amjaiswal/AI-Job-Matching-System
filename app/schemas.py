from pydantic import BaseModel
from typing import List


# -----------------------------
# Match API
# -----------------------------

class MatchRequest(BaseModel):
    student_id: int
    job_id: int


class MatchResponse(BaseModel):
    student_id: int
    student_name: str
    job_id: int
    company: str
    role: str
    eligible: bool
    match_score: float
    reason: str


# -----------------------------
# Rank API
# -----------------------------

class RankRequest(BaseModel):
    job_id: int


class Candidate(BaseModel):
    rank: int
    student_id: int
    student_name: str
    match_score: float
    reason: str