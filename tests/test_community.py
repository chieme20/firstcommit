from firstcommit.community import analyze_community_health


def test_analyze_community_health():
    tree_data = {
        "tree": [
            {"path": "README.md"},
            {"path": "SECURITY.md"},
            {"path": "CHANGELOG.md"},
            {"path": ".github/PULL_REQUEST_TEMPLATE.md"},
            {"path": ".github/ISSUE_TEMPLATE/bug_report.md"},
        ]
    }

    result = analyze_community_health(tree_data)

    assert result["SECURITY.md"] is True
    assert result["CHANGELOG.md"] is True
    assert result["PULL_REQUEST_TEMPLATE.md"] is True
    assert result["ISSUE_TEMPLATE"] is True