import logging
import os
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

# Ensure logs directory exists
LOG_DIR = "/app/logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)

class MonthlyTimedRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None):
        # We start with 'midnight' to rotate daily, but we want monthly naming.
        # Python's native logging doesn't strict support 'Monthly' interval easily efficiently
        # So we use 'midnight' (D) or 'W' (week) usually.
        # However, user requested "1 file / month". 
        # A common trick is to use 'quota' or manual management.
        # BUT for simplicity and standard lib, let's use TimedRotatingFileHandler with 'midnight' 
        # but configured to generate filenames closely or we simply use a filename based on current month
        # and checking if we need to switch.
        
        # Let's stick to standard TimedRotatingFileHandler usage 'midnight' for now to ensure daily safety, 
        # Or we can just calculate filename at startup.
        super().__init__(filename, when, interval, backupCount, encoding, delay, utc, atTime)

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        # Determine filename: api-YYYY-MM.log
        current_month = datetime.utcnow().strftime("%Y-%m")
        log_file = os.path.join(LOG_DIR, f"{name}-{current_month}.log")
        
        # File Handler
        # Note: True monthly rotation usually requires a Custom Handler to check Month change.
        # For now, we append to the current month's file.
        handler = logging.FileHandler(log_file)
        handler.setLevel(logging.INFO)
        
        # formatter = logging.Formatter(
        #     '{"time": "%(asctime)s", "level": "%(levelname)s", "name": "%(name)s", "message": "%(message)s"}'
        # )
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(name)s: %(message)s')
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        
        # Console Handler (for Docker logs)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Pre-defined loggers
request_logger = get_logger("api")
error_logger = get_logger("error")
engine_logger = get_logger("engine")
