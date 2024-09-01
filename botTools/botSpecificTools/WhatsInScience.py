from botTools.reddit.getSubredditPosts import getSubredditPosts


def getWhatsInScienceData():
    redditScienceHotPosts = getSubredditPosts('science')
    over500upvotesPost = [post for post in redditScienceHotPosts if post['upvotes'] > 500]
    return(over500upvotesPost)
