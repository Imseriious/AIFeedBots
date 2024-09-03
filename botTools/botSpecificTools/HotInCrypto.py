from botTools.reddit.getSubredditPosts import getSubredditPosts


def getHotInCryptoRedditData():
    redditCryptoNews = getSubredditPosts('CryptoCurrency', 25, 120, 'GENERAL-NEWS')
    return redditCryptoNews
