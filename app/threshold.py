def validate_threshold(student, job):
    """
    Check whether the student satisfies all the job skill thresholds.
    Returns:
        (eligible: bool, reason: str)
    """

    skills = [
        "python",
        "sql",
        "machine_learning",
        "deep_learning"
    ]

    for skill in skills:
        if student[skill] < job[skill]:
            return False, f"{skill.replace('_', ' ').title()} threshold not met"

    return True, "All skill thresholds satisfied"