#!/usr/bin/python3
"""
0-subs
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = \
        {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)\
          AppleWebKit/537.36(KHTML, like Gecko) \
         Chrome/90.0.4430.93 Safari/537.36'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
