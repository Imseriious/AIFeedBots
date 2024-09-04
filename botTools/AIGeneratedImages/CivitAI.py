import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("CIVITAI_API_KEY");

def getCivitAiImages(period="Day", sort="Most Reactions", limit=10, nsfw="None"):
    url = f"https://civitai.com/api/v1/images?period={period}&sort={sort}&limit={limit}&nsfw={nsfw}"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        structuredData = []
        for item in data['items']:
            structuredItem = {
                'username': item['username'],
                'postUrl': f"https://civitai.com/images/{item['id']}",
                'imageUrl': item['url']
            }
            structuredData.append(structuredItem)
        return structuredData

    else:
        print(f"Failed to retrieve data: {response.status_code}")
        print(response.text)