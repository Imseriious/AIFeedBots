import praw

def initialize_reddit_client():
    return praw.Reddit(
        client_id="bLKGLnJR0l1DxwMyRRDFwA",
        client_secret="S4zikgBp8CKkzszjaqoaXP4ta5P63Q",
        password="Random_1234",
        user_agent="testscript by u/LUCKY777LOSTITALL",
        username="LUCKY777LOSTITALL",
    )
    
def get_subreddit_posts(reddit, subreddit_name, limit=10):
    subreddit = reddit.subreddit(subreddit_name)
    return list(subreddit.hot(limit=limit))