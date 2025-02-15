#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts 
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints the titles of the first 10 hot posts or None for invalid 
        subreddits.
    """
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(base_url, headers=headers,
                                allow_redirects=False)
        
        # Check if the response status code indicates success (200)
        if response.status_code == 200:
            data = response.json()
            # Get the list of posts
            posts = data['data']['children']
            # Print the titles of the first 10 hot posts
            for post in posts[:10]:
                print(post['data']['title'])
        else:
            print(None)
    except Exception as e:
        print(None)
