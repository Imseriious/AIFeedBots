from botTools.botSpecificTools.BestAIPics import getPopularCivitAIPic
from db.createPost import createPost
from datetime import datetime, timezone

def noLLMPost(botName, botId):
    current_datetime = datetime.now(timezone.utc)

    newPostData = {
        "botId": botId,
        "text": "",
        "tags": [],
        "upvotes": 0,
        "creationDate": current_datetime
    }
    
    match botName:
        case 'BestAIPics':
            randomPopularPostFormCivit =  getPopularCivitAIPic()
            newPostData['text'] = f"AI-Generated image by {randomPopularPostFormCivit['username']}"
            newPostData['url'] = randomPopularPostFormCivit['postUrl']
            newPostData['imageUrl'] = randomPopularPostFormCivit['imageUrl']
    createPost(newPostData)