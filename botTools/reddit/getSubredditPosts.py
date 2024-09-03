
from botTools.reddit.redditUtils import get_subreddit_posts, initialize_reddit_client

def getSubredditPosts(subreddit_name, limit, min_upvotes, flair):
    reddit = initialize_reddit_client();
    posts = get_subreddit_posts(reddit, subreddit_name, limit)
    
    if min_upvotes:
        posts = [post for post in posts if post['upvotes'] > min_upvotes]
    if flair:
        posts = [post for post in posts if post['flair'] == flair]
    return posts

