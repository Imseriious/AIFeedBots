
from botTools.botSpecificTools.WhatsInScience import getWhatsInScienceData
from botTools.reddit.getSubredditPosts import getSubredditPosts
from controllers.bots.createNewBot import createNewBot
from controllers.bots.createNewPost import createNewPost

# --- List of bots ---
# RolandWorthington
# CryptoSlave
# WhatsInScience

# --- Available Functions ----
    #createNewBot()
    #createNewPost('RolandWorthington')
    #posts = getSubredditPosts('ArtificialInteligence')
    
def main():
    print("...:::Starting main function:::...")
    createNewPost('WhatsInScience')

main()