import time
import sys
import logging
from logger import setup_logger
from api import fetch_crypto_data
from analysis import analyze_data
from excel_writer import save_to_excel

def main():
    """
    Main function to track cryptocurrency data continuously.
    Fetches data, analyzes it, and saves to Excel every 5 minutes.
    """
    setup_logger()
    
    logging.info("Cryptocurrency Tracker Started")
    
    try:
        while True:
            try:
                crypto_data = fetch_crypto_data()
                
                if not crypto_data:
                    logging.warning("No data fetched. Retrying in 1 minute.")
                    time.sleep(60)
                    continue
                
                df, top_5, average_price, highest_change, lowest_change = analyze_data(crypto_data)
                
                save_to_excel(df, top_5, average_price, highest_change, lowest_change)
                
                logging.info("Waiting 5 minutes for next data fetch...")
                time.sleep(300) 
            
            except Exception as inner_error:
                logging.error(f"Error in main loop: {inner_error}")
                time.sleep(60) 
    
    except KeyboardInterrupt:
        logging.info("Cryptocurrency Tracker Stopped by User")
        sys.exit(0)

if __name__ == "__main__":
    main()