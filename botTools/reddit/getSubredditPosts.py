
from botTools.reddit.redditUtils import get_subreddit_posts, initialize_reddit_client

def getSubredditPosts(subreddit_name, limit=10, min_upvotes=0):
    reddit = initialize_reddit_client();
    posts = get_subreddit_posts(reddit, subreddit_name, limit)
    postsWithMinUpvotes = [post for post in posts if post['upvotes'] > min_upvotes]
    return postsWithMinUpvotes

