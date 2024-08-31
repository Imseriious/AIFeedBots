from llm.bots.getBotPrompt import getBotPrompt
from llm.promptsUtils.delimiters import CHARACTER_DELIMITER
from llm.bots.getBotPrompt import getBotPrompt
from llm.mainPrompts.postGeneralPrompts import generalPostInstructions, negativePrompt

def generatePostPrompt(botName):
    
    characterPrompt = getBotPrompt(botName)
    
    return f"""
    {generalPostInstructions}
    
    {negativePrompt}
    
    The details of the characters will be delimited by {CHARACTER_DELIMITER}
    
    {CHARACTER_DELIMITER}
    {characterPrompt}
    {CHARACTER_DELIMITER}
    """