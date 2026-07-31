from firstcommit.files import analyze_onboarding_files


def test_analyze_onboarding_files():
    tree_data = {
        "tree": [
            {"path": "README.md"},
            {"path": "LICENSE"},
            {"path": "src/main.py"},
        ]
    }

    result = analyze_onboarding_files(tree_data)

    assert result["README.md"] is True
    assert result["LICENSE"] is True
    assert result["CONTRIBUTING.md"] is False
    assert result["CODE_OF_CONDUCT.md"] is False
    