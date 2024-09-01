from db.createBot import createBot


def createNewBot():
    print("...:::Creating Bot:::...")
    newBotData = {
        "name": 'WhatsInScience',
        "avatar": '',
        "botDescription": 'Have some science in your feed. Long story short: Cool science news.',
        "creator": 'AI',
        "creatorLink": ''
    }
    createBot(newBotData)
