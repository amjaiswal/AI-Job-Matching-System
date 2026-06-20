import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from app.threshold import validate_threshold
from app.vectorizer import create_student_vector, create_job_vector

# Load datasets
students = pd.read_csv("data/students.csv")
jobs = pd.read_csv("data/jobs.csv")

print("\n========== AI Job Recommendation ==========\n")

for _, student in students.iterrows():

    best_score = -1
    best_job = None
    best_reason = ""

    for _, job in jobs.iterrows():

        # Check Threshold
        eligible, reason = validate_threshold(student, job)

        if not eligible:
            continue

        # Create vectors
        student_vector = create_student_vector(student).reshape(1, -1)
        job_vector = create_job_vector(job).reshape(1, -1)

        # Cosine Similarity
        score = cosine_similarity(student_vector, job_vector)[0][0] * 100

        if score > best_score:
            best_score = score
            best_job = job
            best_reason = reason

    print(f"Student : {student['name']}")

    if best_job is not None:
        print(f"Recommended Company : {best_job['company']}")
        print(f"Role : {best_job['role']}")
        print(f"Match Score : {best_score:.2f}%")
        print(f"Reason : {best_reason}")
    else:
        print("No suitable job found")

    print("-" * 50)