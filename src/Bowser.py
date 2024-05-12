# Import required modules
import subprocess
import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from flask import Flask, request, abort
import html
from dotenv import load_dotenv

# Import functions
from Logger import setup_logging


# Initialize Flask app
app = Flask(__name__)


load_dotenv('.env')

# Get master, process and developer Tokens
MASTER_TOKEN = os.getenv("MASTER_TOKEN")
PROCESS_TOKEN = os.getenv("PROCESS_TOKEN")
DEVELOPER_TOKEN = os.getenv("DEVELOPER_TOKEN")


# Define log directory and file prefix
log_dir = "./logs/Bowser_Logging"
log_file_prefix = "Bowser"

# Setup logging
setup_logging(log_dir, log_file_prefix)


def create_log_dir(log_dir):
    """
    Create a directory for logs.
    """
    try:
        os.makedirs(log_dir, exist_ok=True)
    except Exception as e:
        app.logger.error(f"Failed to create log directory {log_dir}. Error: {e}")
        raise


def setup_logging(log_dir):
    """
    Setup logging for the application.
    """
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


# Main routing
@app.route('/Bowser', methods=['POST'])
def bowser():
    """
    Endpoint to receive messages and execute corresponding scripts.
    """
    # Extract data from request
    json_MASTER_TOKEN = request.json.get('MASTER_TOKEN')
    json_PROCESS_TOKEN = request.json.get('PROCESS_TOKEN')
    json_process_name = request.json.get('process_name')

    # Validate inputs
    if not all([json_MASTER_TOKEN, json_PROCESS_TOKEN, json_process_name]):
        app.logger.error("Invalid input")
        abort(400)  # Bad Request

    # Check for unauthorized access
    if json_MASTER_TOKEN != MASTER_TOKEN or json_PROCESS_TOKEN != PROCESS_TOKEN:
        app.logger.error("Unauthorized access attempt")
        abort(401)  # Unauthorized

    # Receive message from request and sanitize it
    message = html.escape(request.json.get('message'))
    app.logger.info(f"Received message: {message} for process: {json_process_name}")

    # Execute the appropriate script based on process name
    try:
        subprocess.run(['python', f'./src/PyRocesses/API-Triggered/Enabled/{json_process_name}/{json_process_name}.py', message], check=True)
        app.logger.info(f"Process completed successfully: {json_process_name}.py")
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Failed to execute {json_process_name}.py: {e}")
        return f"Failed to execute {json_process_name}.py: {e}", 500

    return f"Message received and processed by {json_process_name}", 200


# Developer routing
@app.route('/Bowser_DEV', methods=['POST'])
def bowser_dev():
    """
    Endpoint to receive messages and execute corresponding scripts.
    """
    # Extract data from request
    json_MASTER_TOKEN = request.json.get('MASTER_TOKEN')
    json_DEVELOPER_TOKEN = request.json.get('DEVELOPER_TOKEN')
    json_PROCESS_TOKEN = request.json.get('PROCESS_TOKEN')
    json_process_name = request.json.get('process_name')

    # Validate inputs
    if not all([json_MASTER_TOKEN, json_DEVELOPER_TOKEN, json_PROCESS_TOKEN, json_process_name]):
        app.logger.error("Invalid input, check tokens or process name")
        abort(400)  # Bad Request

    # Check for unauthorized access
    if json_MASTER_TOKEN != MASTER_TOKEN or json_DEVELOPER_TOKEN != DEVELOPER_TOKEN or json_PROCESS_TOKEN != PROCESS_TOKEN:
        app.logger.error("Unauthorized access attempt")
        abort(401)  # Unauthorized

    # Receive message from request and sanitize it
    message = html.escape(request.json.get('message'))
    app.logger.info(f"Received message: {message} for process: {json_process_name}")

    # Execute the appropriate script based on process name
    try:
        subprocess.run(['python', f'./src/PyRocesses/API-Triggered/Developer_Tools/{json_process_name}/{json_process_name}.py', message], check=True)
        app.logger.info(f"Process completed successfully: {json_process_name}.py")
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Failed to execute {json_process_name}.py: {e}")
        return f"Failed to execute {json_process_name}.py: {e}", 500

    return f"Message received and processed by {json_process_name}", 200


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)