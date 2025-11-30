from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message: str):
    logging.info(message)

def log_error(message: str):
    logging.error(message)

def format_response(data: dict) -> dict:
    """Format the response data to ensure consistency."""
    return {
        "status": "success",
        "data": data,
        "timestamp": datetime.utcnow().isoformat()
    }

def format_error(message: str) -> dict:
    """Format the error message for consistency."""
    return {
        "status": "error",
        "message": message,
        "timestamp": datetime.utcnow().isoformat()
    }