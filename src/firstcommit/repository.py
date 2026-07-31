from firstcommit.github_api import (
    get_repository,
    get_repository_tree,
)
from firstcommit.scoring import calculate_readiness_score
from firstcommit.files import analyze_onboarding_files


def analyze_repository(owner: str, repository: str) -> dict:
    """
    Retrieve repository information from GitHub
    and calculate its contributor readiness score.
    """

    repository_data = get_repository(owner, repository)

    tree_data = get_repository_tree(owner, repository)

    onboarding_files = analyze_onboarding_files(tree_data)

    score_result = calculate_readiness_score(repository_data)

    return {
        "full_name": repository_data["full_name"],
        "description": repository_data.get("description"),
        "score": score_result["score"],
        "readiness": score_result["readiness"],
        "checks": score_result["checks"],
        "onboarding_files": onboarding_files,
    }