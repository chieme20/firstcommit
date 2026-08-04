# FirstCommit User Guide

## What is FirstCommit?

FirstCommit is a Python CLI application that analyzes GitHub repositories and evaluates how ready they are for contributors.

It checks repository metadata, onboarding files, and community health indicators to generate a contributor readiness score.

---

## Prerequisites

Before using FirstCommit, ensure you have:

- Python 3.11 or higher
- Git installed
- Internet connection

---

## Installation

### Clone the repository

```bash
git clone https://github.com/chieme20/firstcommit.git
cd firstcommit
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux/macOS

```bash
source .venv/bin/activate
```

### Install the package

```bash
pip install -e .
```

---

## Running FirstCommit

Analyze a repository:

```bash
firstcommit owner/repository
```

Example:

```bash
firstcommit chieme20/firstcommit
```

---

## Example Output

```text
Repository: chieme20/firstcommit
Score: 50
Readiness: Fair

Metadata Score: 37.5
Onboarding Score: 12.5
```

---

## What FirstCommit Checks

### Repository Metadata

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
- ISSUE_TEMPLATE
- PULL_REQUEST_TEMPLATE

---

## Running Tests

```bash
pytest
```

---

## Reporting Issues

If you find a bug or have a suggestion, please create an issue in the repository.