#!/usr/bin/python3
"""This lists 10 commits from a
github repository(recent to oldest)
Takes two argument, repo name and username
"""

import requests
import sys

if __name__ == "__main__":
    # Get repository and user names from command-line arguments
    user = sys.argv[2]
    repos = sys.argv[1]

    # Construct the GitHub API URL for retrieving commits
    url = f"https://api.github.com/repos/{user}/{repos}/commits"

    # Send a GET request to the GitHub API
    response = requests.get(url, params={'per_page': 10})

    # Parse the JSON response
    commits = response.json()

    # Iterate through the list of commits and print information
    for commit in commits:
        sha = commit["sha"]
        author_name = commit["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")

        # date = commit["commit"]["author"]["date"]  # for date commit date
        print(f"{sha}: {author_name} {date}")
