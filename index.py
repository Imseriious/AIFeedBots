
from botTools.reddit.getSubredditPosts import getSubredditPosts
from controllers.bots.createNewBot import createNewBot
from controllers.bots.createNewPost import createNewPost

# --- List of bots ---
# RolandWorthington
# CryptoSlave

# --- Available Functions ----
    #createNewBot()
    #createNewPost('RolandWorthington')
    
def main():
    print("...:::Starting main function:::...")
    posts = getSubredditPosts('ArtificialInteligence')

main()