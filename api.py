import requests
import logging
from typing import List, Dict

def fetch_crypto_data() -> List[Dict]:
    """
    Fetch the live cryptocurrency data from the CoinGecko API.
    
    Returns:
        list: List of dictionaries containing the cryptocurrency data.
    """
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 50, 
            "page": 1,
            "sparkline": False,
            "price_change_percentage": "24h"
        }
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status() 
        
        logging.info(f"Successfully fetched data for top 50 cryptocurrencies")
        
        return response.json()
    
    except requests.RequestException as e:
        logging.error(f"Error fetching cryptocurrency data: {e}")
        return []