def calculate_readiness_score(repository: dict) -> dict:
    """
    Calculate a contributor readiness score based on
    GitHub repository metadata.
    """

    score = 0

    checks = {
        "description": bool(repository.get("description")),
        "license": bool(repository.get("license")),
        "issues_enabled": repository.get("has_issues", False),
        "public_repository": not repository.get("private", True),
    }

    for passed in checks.values():
        if passed:
            score += 25

    if score >= 90:
        readiness = "Excellent"

    elif score >= 70:
        readiness = "Good"

    elif score >= 50:
        readiness = "Fair"

    else:
        readiness = "Needs Improvement"

    return {
        "score": score,
        "readiness": readiness,
        "checks": checks,
    }