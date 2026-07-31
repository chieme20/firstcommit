import requests


def get_repository(owner: str, repository: str) -> dict:
    """
    Retrieve basic information about a GitHub repository.

    Args:
        owner: The GitHub username or organisation that owns the repository.
        repository: The name of the GitHub repository.

    Returns:
        A dictionary containing the repository information.

    Raises:
        requests.HTTPError: If GitHub returns an unsuccessful response.
    """

    url = f"https://api.github.com/repos/{owner}/{repository}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


def get_repository_tree(owner: str, repository: str) -> dict:
    """
    Retrieve the complete file tree of a GitHub repository.
    """

    repository_data = get_repository(owner, repository)

    default_branch = repository_data["default_branch"]

    url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repository}/git/trees/"
        f"{default_branch}?recursive=1"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()