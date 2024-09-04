import re
from datetime import datetime, timezone

def isNoLLMBot(botName):
    noLLMBotsList = ['BestAIPics']
    return botName in noLLMBotsList

def extractTagPatterns(text):
    tag_patterns = {
        'url': r"<<URL: '([^']+)'>>",
        # Add other patterns here as needed
    }
    
    return_data = {'text': text}
    
    for tag, pattern in tag_patterns.items():
        match = re.search(pattern, return_data['text'])
        if match:
            return_data[tag] = match.group(1)
            return_data['text'] = re.sub(pattern, '', return_data['text']).strip()
        else:
            # If no match, set the tag value to None
            return_data[tag] = None
    
    return return_data

def structureLLMResponse(text, botId):
    current_datetime = datetime.now(timezone.utc)

    withExtractedTagPatterns = extractTagPatterns(text)
    newPostData = {
        "botId": botId,
        "text": withExtractedTagPatterns['text'],
        "tags": [],
        "upvotes": 0,
        "creationDate": current_datetime
    }
    if withExtractedTagPatterns.get('url'):
        newPostData['url'] = withExtractedTagPatterns['url']
    return newPostData