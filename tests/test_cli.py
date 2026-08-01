from firstcommit.cli import main


def test_cli_help(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["firstcommit", "--help"],
    )

    try:
        main()
    except SystemExit:
        pass

    captured = capsys.readouterr()

    assert "Analyze GitHub repository readiness" in captured.out