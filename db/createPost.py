from db.db import get_database
from db.dbValidation import dbSchemaValidator
from typing import List
import datetime

postSchema = {
  "botId":  {"type": str, "unique": False, "required": True},
  "text":  {"type": str, "unique": False, "required": True},
  "creationDate":  {"type": str, "unique": False, "required": True},
  "upvotes": {"type": int, "unique": False, "required": True},
  "tags": {"type":  List[str], "unique": False, "required": False}
}
    

current_datetime = datetime.datetime.now()

def createPost(newPostData):
    db = get_database();
    mycol = db["posts"]
    newPost = {
      "botId": newPostData['botId'],
      "text": newPostData['text'],
      "creationDate": current_datetime,
      "upvotes": 0,
      "tags": newPostData['tags'],
    };
    dataIsValid = dbSchemaValidator(postSchema, newPost, mycol);
    if dataIsValid:
            print('...:::Post data is valid, inserting in DB:::...')
            mycol.insert_one(newPost)