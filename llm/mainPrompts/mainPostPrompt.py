from llm.bots.getBotPrompt import getBotPrompt
from llm.promptsUtils.delimiters import CHARACTER_DELIMITER, POST_HISTORY_DELIMITER, DATA_TO_USE_DELIMITED
from llm.bots.getBotPrompt import getBotPrompt
from llm.mainPrompts.mainPostPromptUtils import generalPostInstructions, negativePrompt, delimitersPrompt

def mainPostPrompt(botName, last10Posts, dataForLLM):
    
    characterPrompt = getBotPrompt(botName)
    if(characterPrompt):
        prompt =  f"""
        {generalPostInstructions}
        
        {negativePrompt}
        
        {delimitersPrompt}
        
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
        if dataForLLM:
            prompt += f"""
                \nHere is the data you have to use: 
                
                {DATA_TO_USE_DELIMITED}
                
                {dataForLLM}
                
                {DATA_TO_USE_DELIMITED}
            """
        
        return prompt