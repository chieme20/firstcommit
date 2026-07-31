def analyze_onboarding_files(tree_data: dict) -> dict:
    """
    Analyze a repository tree and check whether
    important onboarding files exist.
    """

    paths = {
        item["path"].upper()
        for item in tree_data.get("tree", [])
    }

    return {
        "README.md": "README.MD" in paths,
        "LICENSE": "LICENSE" in paths,
        "CONTRIBUTING.md": "CONTRIBUTING.MD" in paths,
        "CODE_OF_CONDUCT.md": (
            "CODE_OF_CONDUCT.MD" in paths
            or ".GITHUB/CODE_OF_CONDUCT.MD" in paths
        ),
    }