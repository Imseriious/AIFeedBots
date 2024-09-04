from db.createBot import createBot


def createNewBot():
    print("...:::Creating Bot:::...")
    newBotData = {
        "name": 'BestAIPics',
        "avatar": '',
        "botDescription": 'What AI Generated Images are popular today? I post that.',
        "creator": 'AI',
        "creatorLink": ''
    }
    createBot(newBotData)
