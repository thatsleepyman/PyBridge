import subprocess
import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from flask import Flask, request, abort

app = Flask(__name__)

# Define master password and process password
MASTER_PASSWORD = os.getenv("MASTER_PASSWORD")
PROCESS_PASSWORD = os.getenv("PROCESS_PASSWORD")

def create_log_dir(log_dir):
    try:
        os.makedirs(log_dir, exist_ok=True)
    except Exception as e:
        app.logger.error(f"Failed to create log directory {log_dir}. Error: {e}")
        raise

def setup_logging(log_dir):
    create_log_dir(log_dir)

    log_file = f"{log_dir}/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_Bowser.log"
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
    file_handler.setFormatter(formatter)

    try:
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
    except Exception as e:
        app.logger.error(f"Failed to setup logger. Error: {e}")
        raise

# Usage
log_dir = "./Log/Bowser_Logging"
setup_logging(log_dir)

@app.route('/Bowser', methods=['POST'])
def bowser():
    # Check if master and process password is provided
    json_master_password = request.json.get('master_password')
    json_process_password = request.json.get('process_password')
    # Get process_name to decide what script to send the message to
    json_process_name = request.json.get('process_name')

    # Validate inputs
    if not all([json_master_password, json_process_password, json_process_name]):
        app.logger.error("Invalid input")
        abort(400)  # Bad Request

    if json_master_password != MASTER_PASSWORD or json_process_password != PROCESS_PASSWORD:
        app.logger.error("Unauthorized access attempt")
        abort(401)  # Unauthorized

    # Receive message from request
    message = request.json.get('message')
    app.logger.info(f"Received message: {message} for process: {json_process_name}")

    # Forward message to PyRocess_Handler.py for processing
    process_message(json_process_password, json_process_name, message)
    
    return f"Message received and forwarded to PyRocess_Handler to trigger {json_process_name}", 200

def process_message(json_process_password, json_process_name, message):
    try:
        # Execute PyRocess_Handler.py and pass the message as an argument
        subprocess.run(['python', 'PyRocess_Handler.py', json_process_password, json_process_name, message], check=True)
        app.logger.info(f"Message forwarded to PyRocess_Handler for process: {json_process_name}")
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Failed to trigger {json_process_name}: {e}")


if __name__ == '__main__':
    app.run(debug=True)