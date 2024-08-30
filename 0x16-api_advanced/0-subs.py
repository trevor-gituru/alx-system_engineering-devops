#!/usr/bin/python3
"""
Query Reddit API for number of subscribers for a given subreddit
"""
from json import loads
import requests
import sys


def number_of_subscribers(subreddit):
    """ecursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return None
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 2
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    reddits = response.json()

    try:
        subscribers = reddits.get('data').get('subscribers')
        return int(subscribers)
    except:
        return 0
