from llm.bots.getBotPrompt import getBotPrompt
from llm.promptsUtils.delimiters import CHARACTER_DELIMITER, POST_HISTORY_DELIMITER
from llm.bots.getBotPrompt import getBotPrompt
from llm.mainPrompts.postGeneralPrompts import generalPostInstructions, negativePrompt

def generatePostPrompt(botName, last10Posts):
    
    characterPrompt = getBotPrompt(botName)
    if(characterPrompt):
        prompt =  f"""
        {generalPostInstructions}
        
        {negativePrompt}
        
        The details of the characters will be delimited by {CHARACTER_DELIMITER}
        Your historical posts will be delimited by {POST_HISTORY_DELIMITER}
        
        {CHARACTER_DELIMITER}
        {characterPrompt}
        {CHARACTER_DELIMITER}
        """
        
        if last10Posts:
            prompt += f"""
                \nHere are the last 10 posts: 
                
                {POST_HISTORY_DELIMITER}
                
                {last10Posts}
                
                {POST_HISTORY_DELIMITER}
            """
        
        return prompt