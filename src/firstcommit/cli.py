import argparse
import requests

from firstcommit.repository import analyze_repository


def main():
    parser = argparse.ArgumentParser(
        description="Analyze GitHub repository readiness."
    )

    parser.add_argument(
        "repository",
        help="Repository in the format owner/repository",
    )

    args = parser.parse_args()

    owner, repository = args.repository.split("/")

    try:
        result = analyze_repository(owner, repository)

    except requests.HTTPError:
        print()
        print("Error: Repository not found.")
        return

    print()
    print(f"Repository: {result['full_name']}")
    print(f"Score: {result['score']}")
    print(f"Readiness: {result['readiness']}")
    print()
    print(f"Metadata Score: {result['metadata_score']}")
    print(f"Onboarding Score: {result['onboarding_score']}")
    print()

    print("Onboarding Files:")

    for file_name, exists in result["onboarding_files"].items():
        status = "✓" if exists else "✗"
        print(f"{file_name:<20} {status}")


if __name__ == "__main__":
    main()