from firstcommit.github_api import get_repository
from firstcommit.scoring import calculate_readiness_score


def analyze_repository(owner: str, repository: str) -> dict:
    """
    Retrieve repository information from GitHub
    and calculate its contributor readiness score.
    """

    repository_data = get_repository(owner, repository)

    score_result = calculate_readiness_score(repository_data)

    return {
        "full_name": repository_data["full_name"],
        "description": repository_data.get("description"),
        "score": score_result["score"],
        "readiness": score_result["readiness"],
        "checks": score_result["checks"],
    }