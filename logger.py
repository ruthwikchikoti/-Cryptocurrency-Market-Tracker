import logging
from datetime import datetime
import os

log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

def setup_logger():
    log_filename = os.path.join(log_dir, f'crypto_tracker_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
    
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter('%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', 
                                                   datefmt='%Y-%m-%d %H:%M:%S'))
    
    root_logger = logging.getLogger()
    root_logger.addHandler(console_handler)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

def log_warning(message):
    logging.warning(message)