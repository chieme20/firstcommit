def analyze_community_health(tree_data: dict) -> dict:
    """
    Analyze community and security related files.
    """

    file_paths = {
        item["path"]
        for item in tree_data.get("tree", [])
    }

    return {
        "SECURITY.md": "SECURITY.md" in file_paths,
        "CHANGELOG.md": "CHANGELOG.md" in file_paths,
        "PULL_REQUEST_TEMPLATE.md":
            ".github/PULL_REQUEST_TEMPLATE.md" in file_paths,
        "ISSUE_TEMPLATE":
            any(
                path.startswith(".github/ISSUE_TEMPLATE/")
                for path in file_paths
            ),
    }