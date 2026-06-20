import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from app.threshold import validate_threshold
from app.vectorizer import create_student_vector, create_job_vector

# ============================================
# Load Datasets
# ============================================

students = pd.read_csv("data/students.csv")
jobs = pd.read_csv("data/jobs.csv")


# ============================================
# Match One Student with One Job
# ============================================

def get_match(student_id: int, job_id: int):

    student_df = students[students["student_id"] == student_id]

    if student_df.empty:
        raise ValueError("Student Not Found")

    job_df = jobs[jobs["job_id"] == job_id]

    if job_df.empty:
        raise ValueError("Job Not Found")

    student = student_df.iloc[0]
    job = job_df.iloc[0]

    # Threshold Validation
    eligible, reason = validate_threshold(student, job)

    if not eligible:

        return {
            "student_id": student_id,
            "job_id": job_id,
            "eligible": False,
            "match_score": 0,
            "reason": reason
        }

    # Create Vectors
    student_vector = create_student_vector(student).reshape(1, -1)
    job_vector = create_job_vector(job).reshape(1, -1)

    # Cosine Similarity
    score = round(
        cosine_similarity(student_vector, job_vector)[0][0] * 100,
        2
    )

    return {

        "student_id": int(student["student_id"]),

        "student_name": student["name"],

        "job_id": int(job["job_id"]),

        "company": job["company"],

        "role": job["role"],

        "eligible": True,

        "match_score": score,

        "reason": reason

    }


# ============================================
# Rank Candidates for One Job
# ============================================

def rank_candidates(job_id: int):

    job_df = jobs[jobs["job_id"] == job_id]

    if job_df.empty:
        raise ValueError("Job Not Found")

    job = job_df.iloc[0]

    rankings = []

    for _, student in students.iterrows():

        eligible, reason = validate_threshold(student, job)

        if not eligible:
            continue

        student_vector = create_student_vector(student).reshape(1, -1)
        job_vector = create_job_vector(job).reshape(1, -1)

        score = round(
            cosine_similarity(student_vector, job_vector)[0][0] * 100,
            2
        )

        rankings.append({

            "student_id": int(student["student_id"]),

            "student_name": student["name"],

            "match_score": score,

            "reason": reason

        })

    rankings = sorted(

        rankings,

        key=lambda x: x["match_score"],

        reverse=True

    )

    for index, candidate in enumerate(rankings, start=1):

        candidate["rank"] = index

    return rankings