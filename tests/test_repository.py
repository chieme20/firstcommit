from firstcommit.repository import analyze_repository


def test_analyze_repository(mocker):
    fake_repository = {
        "full_name": "chieme20/firstcommit",
        "description": "Test repository",
        "license": None,
        "has_issues": True,
        "private": False,
    }

    mocker.patch(
        "firstcommit.repository.get_repository",
        return_value=fake_repository,
    )

    result = analyze_repository("chieme20", "firstcommit")

    assert result["full_name"] == "chieme20/firstcommit"
    assert result["score"] == 75
    assert result["readiness"] == "Good"
    assert result["checks"]["description"] is True
    assert result["checks"]["license"] is False
    