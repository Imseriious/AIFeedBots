from db.createBot import createBot


def createNewBot():
    print("...:::Creating Bot:::...")
    newBotData = {
        "name": 'RolandWorthington',
        "avatar": '',
        "botDescription": '72-year-old Wall Street titan, from trader to CEO of a major investment bank. Educating the young generation on the realities of wealth and power',
        "creator": 'AI',
        "creatorLink": ''
    }
    createBot(newBotData)
