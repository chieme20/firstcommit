def calculate_readiness_score(
    repository: dict,
    onboarding_files: dict,
) -> dict:
    """
    Calculate an overall contributor readiness score
    based on repository metadata and onboarding files.
    """

    metadata_checks = {
        "description": bool(repository.get("description")),
        "license": bool(repository.get("license")),
        "issues_enabled": repository.get("has_issues", False),
        "public_repository": not repository.get("private", True),
    }

    metadata_score = 0

    for passed in metadata_checks.values():
        if passed:
            metadata_score += 12.5

    onboarding_score = 0

    for passed in onboarding_files.values():
        if passed:
            onboarding_score += 12.5

    total_score = int(metadata_score + onboarding_score)

    if total_score >= 90:
        readiness = "Excellent"

    elif total_score >= 75:
        readiness = "Good"

    elif total_score >= 50:
        readiness = "Fair"

    else:
        readiness = "Needs Improvement"

    return {
        "score": total_score,
        "readiness": readiness,
        "metadata_score": metadata_score,
        "onboarding_score": onboarding_score,
        "checks": metadata_checks,
    }