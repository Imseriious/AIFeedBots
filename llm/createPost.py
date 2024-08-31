import anthropic
from dotenv import load_dotenv
import os
from llm.mainPrompts.generatePostPrompt import generatePostPrompt

load_dotenv()  # take environment variables from .env.

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

def createPostLLMResponse(botName):
    # Generate the system message using the generatePostPrompt function
    systemMessage = generatePostPrompt(botName)

    # Define the number of posts to create
    numberOfPostsToCreate = 5

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