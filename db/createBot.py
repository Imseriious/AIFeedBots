from db.db import get_database
from db.dbValidation import dbSchemaValidator
import datetime

botSchema = {
    "name": {"type": str, "unique": True, "required": True},
    "avatar": {"type": str, "unique": False, "required": False},
    "botDescription": {"type": str, "unique": True, "required": True},
    "creator": {"type": str, "unique": False, "required": True},
    "followers": {"type": int, "unique": False, "required": True},
    "creationDate": {"type": str, "unique": False, "required": True},
    "creatorLink": {"type": str, "unique": False, "required": False}
}

current_datetime = datetime.datetime.now()

def createBot(newBotData):
    db = get_database()
    mycol = db["bots"]
    newBot = {
        "name": newBotData['name'],
        "avatar": newBotData['avatar'],
        "botDescription": newBotData['botDescription'],
        "creator": newBotData['creator'],
        "followers": 0,
        "creationDate": current_datetime,
        "creatorLink": newBotData['creatorLink']
    }
    try:
        dataIsValid = dbSchemaValidator(botSchema, newBot, mycol)
        if dataIsValid:
            print('...:::Bot data is valid, inserting in DB:::...')
            mycol.insert_one(newBot)
            return True
    except ValueError as e:
        print(f"Validation failed: {str(e)}")
        return False