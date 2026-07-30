from firstcommit.github_api import get_repository


def test_get_repository(mocker):
    mock_response = mocker.Mock()

    mock_response.json.return_value = {
        "full_name": "chieme20/firstcommit",
        "description": "Test repository",
        "stargazers_count": 0,
    }

    mock_response.raise_for_status.return_value = None

    mocker.patch(
        "firstcommit.github_api.requests.get",
        return_value=mock_response,
    )

    result = get_repository("chieme20", "firstcommit")

    assert result["full_name"] == "chieme20/firstcommit"
    assert result["description"] == "Test repository"
    assert result["stargazers_count"] == 0