import anthropic
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    system="System message",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Create a very short post for the world to hear your message"
                }
            ]
        }
    ]
)
print(message.content)