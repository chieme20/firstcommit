# FirstCommit

[![Python Tests](https://github.com/chieme20/firstcommit/actions/workflows/python-tests.yml/badge.svg)](https://github.com/chieme20/firstcommit/actions/workflows/python-tests.yml)

An open-source contributor onboarding simulator and repository readiness analysis tool.

## Usage

Analyze a GitHub repository from the command line:

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
```

If a repository does not exist:

```bash
firstcommit fakeuser/fakerepo
```

Output:

```text
Error: Repository not found.
```