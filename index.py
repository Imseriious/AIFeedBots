
from botTools.botSpecificTools.HotInCrypto import getHotInCryptoRedditData
from botTools.botSpecificTools.WhatsInScience import getWhatsInScienceData
from botTools.reddit.getSubredditPosts import getSubredditPosts
from controllers.bots.createNewBot import createNewBot
from controllers.bots.createNewPost import createNewPost

# --- List of bots ---
# Top10Cryptos
# WhatsInScience
# HotInCrypto

# --- Available Functions ----
    #createNewBot()
    #createNewPost('Top10Cryptos')
    #posts = getSubredditPosts('ArtificialInteligence')
    
def main():
    print("...:::Starting main function:::...")
    createNewPost("HotInCrypto")

main()