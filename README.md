# firstcommit
An open-source contributor onboarding simulator that evaluates how easily a new developer can understand, set up, and contribute to a GitHub project.

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