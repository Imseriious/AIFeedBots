import anthropic
from dotenv import load_dotenv
import os
from llm.mainPrompts.mainPostPrompt import mainPostPrompt

load_dotenv()  # take environment variables from .env.

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

def createPostLLMResponse(botName, last10Posts, dataForLLM):
    #Todo: Instead of passing the last 10 posts, you should create a resume of all the subjects that have been discussed in the past posts, to reduce token size in the prompt.
    systemMessage = mainPostPrompt(botName, last10Posts, dataForLLM)
    print(systemMessage)
    if(systemMessage):
        numberOfPostsToCreate = 1

        # Create the message payload
        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            temperature=1,
            system=systemMessage,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Create a number of {numberOfPostsToCreate} posts"
                        }
                    ]
                }
            ]
        )

        return message.content[0].text
    return
