from botTools.reddit.getSubredditPosts import getSubredditPosts


def getWhatsInScienceData():
    redditScienceHotPosts = getSubredditPosts('science', 10, 500)
    return(redditScienceHotPosts)
