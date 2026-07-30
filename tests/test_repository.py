from firstcommit.repository import analyze_repository


def test_analyze_repository():
    result = analyze_repository(
        "https://github.com/chieme20/firstcommit"
    )

    assert result["repository_url"] == (
        "https://github.com/chieme20/firstcommit"
    )
    assert result["status"] == "ready"
    