import pandas as pd
import logging
from typing import Tuple, Dict

def analyze_data(crypto_data: list) -> Tuple[pd.DataFrame, pd.DataFrame, float, Dict, Dict]:
    """
    Perform comprehensive data analysis on the cryptocurrency data.
    
    Args:
        crypto_data (list): List of dictionaries containing cryptocurrency data.
        
    Returns:
        tuple: Dataframe of all data, top 5 cryptos, average price, highest change, and lowest change.
    """
    if not crypto_data:
        logging.warning("No cryptocurrency data to analyze")
        return pd.DataFrame(), pd.DataFrame(), 0.0, {}, {}
    
    try:
        columns_to_keep = [
            'name', 'symbol', 'current_price', 'market_cap', 
            'total_volume', 'price_change_percentage_24h'
        ]
        df = pd.DataFrame(crypto_data)[columns_to_keep]
        
        df.columns = [
            'Name', 'Symbol', 'Current Price (USD)', 
            'Market Cap', 'Trading Volume', 'Price Change (%)'
        ]
        
        top_5 = df.nlargest(5, 'Market Cap')
        
        average_price = df['Current Price (USD)'].mean()
        
        highest_change = df.loc[df['Price Change (%)'].idxmax()]
        lowest_change = df.loc[df['Price Change (%)'].idxmin()]
        
        logging.info(f"Analysis complete. Average Price: ${average_price:.2f}")
        logging.info(f"Highest 24h Change: {highest_change['Name']} ({highest_change['Price Change (%)']:.2f}%)")
        logging.info(f"Lowest 24h Change: {lowest_change['Name']} ({lowest_change['Price Change (%)']:.2f}%)")
        
        return df, top_5, average_price, highest_change.to_dict(), lowest_change.to_dict()
    
    except Exception as e:
        logging.error(f"Error in data analysis: {e}")
        return pd.DataFrame(), pd.DataFrame(), 0.0, {}, {}