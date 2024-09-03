import praw
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.environ.get("REDDIT_ID");
client_secret = os.environ.get("REDDIT_SECRET");
password = os.environ.get("REDDIT_PASSWORD");
username = os.environ.get("REDDIT_USERNAME");

def initialize_reddit_client():
    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        password=password,
        user_agent="testscript by u/LUCKY777LOSTITALL",
        username=username,
    )
    
def get_subreddit_posts(reddit, subreddit_name, limit=10):
    subreddit = reddit.subreddit(subreddit_name)
    subredditSubmissions = list(subreddit.hot(limit=limit))
    formattedPosts = formatRedditPosts(subredditSubmissions)
    return formattedPosts

def formatRedditPosts(posts):
    formattedPosts = []
    for post in posts:
        formattedPosts.append({
            'title': post.title,
            'url': post.url,
            'upvotes': post.score,
            'text': post.selftext,
            'flair': post.link_flair_text
        })
    return formattedPosts