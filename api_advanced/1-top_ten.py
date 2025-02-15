#!/usr/bin/python3
import requests

def top_ten(subreddit):
    # Define the base URL for the Reddit API
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # Set custom User-Agent to avoid issues with Reddit's API
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        # Send GET request to the Reddit API
        response = requests.get(base_url, headers=headers, allow_redirects=False)
        
        # Check if the response status code indicates success (200)
        if response.status_code == 200:
            data = response.json()
            # Get the list of posts
            posts = data['data']['children']
            # Print the titles of the first 10 hot posts
            for post in posts[:10]:
                print(post['data']['title'])
        else:
            # Print None for invalid subreddits or other issues
            print(None)
    except Exception as e:
        # Print None in case of any exception
        print(None)
