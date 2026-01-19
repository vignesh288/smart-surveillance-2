import logging
import datetime

logging.basicConfig(filename='surveillance.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def log_event(message):
    logging.info(message)