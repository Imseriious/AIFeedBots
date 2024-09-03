
from botTools.botSpecificTools.WhatsInScience import getWhatsInScienceData
from botTools.reddit.getSubredditPosts import getSubredditPosts
from controllers.bots.createNewBot import createNewBot
from controllers.bots.createNewPost import createNewPost

# --- List of bots ---
# Top10Cryptos
# WhatsInScience

# --- Available Functions ----
    #createNewBot()
    #createNewPost('Top10Cryptos')
    #posts = getSubredditPosts('ArtificialInteligence')
    
def main():
    print("...:::Starting main function:::...")
    print(getSubredditPosts('CryptoCurrency'))

main()