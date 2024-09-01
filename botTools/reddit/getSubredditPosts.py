
from botTools.reddit.redditUtils import get_subreddit_posts, initialize_reddit_client

def getSubredditPosts(subreddit_name='worldnews', limit=10):
    reddit = initialize_reddit_client();
    posts = get_subreddit_posts(reddit, subreddit_name, limit)
    formattedPosts = []
    for post in posts:
        formattedPosts.append({
            'title': post.title,
            'url': post.url,
            'upvotes': post.score,
            'text': post.selftext
        })
    return formattedPosts
