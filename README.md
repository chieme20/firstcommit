# FirstCommit

[![Python Tests](https://github.com/chieme20/firstcommit/actions/workflows/python-tests.yml/badge.svg)](https://github.com/chieme20/firstcommit/actions/workflows/python-tests.yml)

An open-source contributor onboarding simulator and repository readiness analysis tool that evaluates how easy it is for new developers to understand, set up, and contribute to a GitHub repository.

## Features

- Analyze GitHub repository metadata
- Check contributor onboarding files
- Evaluate community health files
- Generate a contributor readiness score
- Display repository readiness through a simple CLI
- Automated testing with Pytest
- Continuous Integration with GitHub Actions

## Installation

Clone the repository:

```bash
git clone https://github.com/chieme20/firstcommit.git
cd firstcommit
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install the package:

```bash
pip install -e .
```

## Usage

Analyze a repository:

```bash
firstcommit owner/repository
```

Example:

```bash
firstcommit chieme20/firstcommit
```

Example output:

```text
Repository: chieme20/firstcommit
Score: 50
Readiness: Fair

Metadata Score: 37.5
Onboarding Score: 12.5

Onboarding Files:
README.md            ✓
LICENSE              ✗
CONTRIBUTING.md      ✗
CODE_OF_CONDUCT.md   ✗

Community Health:
SECURITY.md               ✗
CHANGELOG.md              ✗
PULL_REQUEST_TEMPLATE.md  ✗
ISSUE_TEMPLATE            ✗
```

## Readiness Scoring

The project evaluates repositories using:

### Metadata Checks

- Description
- License
- Issues Enabled
- Public Repository

### Onboarding Files

- README.md
- LICENSE
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md

### Community Health Files

- SECURITY.md
- CHANGELOG.md
- PULL_REQUEST_TEMPLATE.md
- ISSUE_TEMPLATE

## Running Tests

```bash
pytest
```

## Continuous Integration

GitHub Actions automatically runs tests on:

- Pushes to `main`
- Pull Requests

## Project Structure

```text
src/
└── firstcommit/
    ├── cli.py
    ├── community.py
    ├── files.py
    ├── github_api.py
    ├── repository.py
    └── scoring.py

tests/
├── test_cli.py
├── test_community.py
├── test_files.py
├── test_github_api.py
└── test_repository.py
```

## Author

Martina Chiemezuo

## License

This project is for educational and open-source learning purposes.