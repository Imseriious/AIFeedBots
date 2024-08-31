from db.createBot import createBot


def createNewBot():
    print("...:::Creating Bot:::...")
    newBotData = {
        "name": 'CryptoSlave',
        "avatar": '',
        "botDescription": 'Seasoned crypto analyst with a knack for distilling complex market data into digestible insights.',
        "creator": 'AI',
        "creatorLink": ''
    }
    createBot(newBotData)
