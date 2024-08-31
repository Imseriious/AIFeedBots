import requests
from dotenv import load_dotenv
import os

load_dotenv() 

def get_top_10_cryptocurrencies():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    
    parameters = {
        'start': '1',
        'limit': '10',
        'sort': 'market_cap',
        'sort_dir': 'desc',
        'convert': 'USD'
    }
    
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': os.environ.get("COINMARKETCAP_API_KEY"),
    }
    
    response = requests.get(url, headers=headers, params=parameters)
    if response.status_code == 200:
        formatted_crypto_data = []
        for crypto in response.json()['data']:
            crypto_info = {
                'name': crypto['name'],
                'symbol': crypto['symbol'],
                'cmc_rank': crypto['cmc_rank'],
                'price': crypto['quote']['USD']['price'],
                'volume_24h': crypto['quote']['USD']['volume_24h'],
                'percent_change_1h': crypto['quote']['USD']['percent_change_1h'],
                'percent_change_24h': crypto['quote']['USD']['percent_change_24h'],
                'percent_change_7d': crypto['quote']['USD']['percent_change_7d'],
                'market_cap': crypto['quote']['USD']['market_cap'],
            }
            formatted_crypto_data.append(crypto_info)
        return formatted_crypto_data
    else:
        return {"error": f"Failed to fetch data. Status code: {response.status_code}"}