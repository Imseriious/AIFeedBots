from db.db import get_database
from db.dbValidation import dbSchemaValidator
from typing import List

postSchema = {
  "botId":  {"type": str, "unique": False, "required": True},
  "text":  {"type": str, "unique": False, "required": True},
  "creationDate":  {"type": str, "unique": False, "required": True},
  "upvotes": {"type": int, "unique": False, "required": True},
  "tags": {"type":  List[str], "unique": False, "required": False},
  "url": {"type":  str, "unique": False, "required": False}
}

def createPost(newPostData):
    db = get_database();
    mycol = db["posts"]
    dataIsValid = dbSchemaValidator(postSchema, newPostData, mycol);
    if dataIsValid:
            print('...:::Post data is valid, inserting in DB:::...')
            mycol.insert_one(newPostData)