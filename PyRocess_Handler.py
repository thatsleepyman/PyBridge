import sys
import subprocess
import logging
import os
from subprocess import CalledProcessError
from datetime import datetime
from html import escape

def setup_logging():
    log_dir = "./Log/PyRocess_Handler_Logging" # Use forward slashes for cross-platform compatibility
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = f"{log_dir}/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_PyRocess_Handler.log"
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main(message):
    setup_logging()

    # Check process password if necessary
    process_password = os.getenv("PROCESS_PASSWORD")
    process_name = sys.argv[2]

    # Validate process password
    json_process_password = sys.argv[1]
    if not json_process_password:
        logging.error("Unauthorized: Incorrect or missing process password")
        return

    if json_process_password != process_password:
        logging.error("Unauthorized: Incorrect process password")
        return

    # Validate process name
    if not process_name:
        logging.error("Invalid process name")
        return

    # Sanitize message to prevent XSS
    sanitized_message = escape(message)

    # Log the incoming request
    logging.info(f"Process started: {process_name}, Message: {sanitized_message}")

    # Execute the appropriate script based on process name
    try:
        subprocess.run(['python', f'{process_name}', sanitized_message], check=True)
        logging.info(f"Process completed successfully: {process_name}")
    except CalledProcessError as e:
        logging.error(f"Failed to execute {process_name}: {e}")
        return


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: PyRocess_Handler.py [process_password] [process_name] [message]")
    else:
        main(sys.argv[3])  # Message is the third argument