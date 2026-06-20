import numpy as np

# List of skills used for vector generation
SKILLS = [
    "python",
    "sql",
    "machine_learning",
    "deep_learning"
]


def create_student_vector(student):
    """
    Convert a student record into a numerical vector.
    """
    return np.array([student[skill] for skill in SKILLS])


def create_job_vector(job):
    """
    Convert a job record into a numerical vector.
    """
    return np.array([job[skill] for skill in SKILLS])
