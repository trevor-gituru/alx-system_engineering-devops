#!/usr/bin/python3
"""
0-subs.py

Task 0

This script defines a function that queries the Reddit API and returns the
number of subscribers for a given subreddit. If the subreddit is invalid,
the function returns 0.

For detailed task description and requirements, refer to the README file.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Task 0

    Queries the Reddit API and returns the number of subscribers for a
    given subreddit. If the subreddit is invalid, returns 0.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: Number of subscribers or 0 if the subreddit is invalid.
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
