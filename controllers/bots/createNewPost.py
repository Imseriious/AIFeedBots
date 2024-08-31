from db.createPost import createPost
from db.db import get_database
from llm.createPost import createPostLLMResponse


def createNewPost(botName):
    print(f"...:::{botName} is creating Post:::...")
    
    db = get_database()
    botsCol = db["bots"]
    postsCol = db["posts"]
    
    botInDb = botsCol.find_one({'name': botName})
    botId = botInDb['_id'];
    
    postsInDb = postsCol.find({'botId': botId})
    formattedStringLast10Posts = None
    if postsInDb:
        textsInPostsArray = [post['text'] for post in postsInDb]

       
        last10Posts = list(textsInPostsArray)[:10]
        
        formattedStringLast10Posts = "\n".join([f"{i + 1}. {text}" for i, text in enumerate(last10Posts)])

        print(formattedStringLast10Posts)
    
    
    if botId:
        llmPost = createPostLLMResponse(botName, formattedStringLast10Posts)
        if(llmPost):
            newPostData = {
                "botId": botId,
                "text": llmPost,
                "tags": [],
            }
            createPost(newPostData)
        else:
          raise ValueError(f"LLM Post not not valid")
   
