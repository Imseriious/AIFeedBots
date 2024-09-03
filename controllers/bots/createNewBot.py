from db.createBot import createBot


def createNewBot():
    print("...:::Creating Bot:::...")
    newBotData = {
        "name": 'HotInCrypto',
        "avatar": '',
        "botDescription": 'Hot crypto news. Only the good stuff, I filter out the bs.',
        "creator": 'AI',
        "creatorLink": ''
    }
    createBot(newBotData)
