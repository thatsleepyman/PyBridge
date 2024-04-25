import subprocess
import os
import logging
from logging.handlers import RotatingFileHandler
from Logger import setup_logging
from datetime import datetime
from flask import Flask, request, abort
import html



# Initialize Flask app
app = Flask(__name__)

# Define master password and process password
# These are environment variables and should be set in the environment where this script runs
MASTER_PASSWORD = os.getenv("MASTER_PASSWORD")
PROCESS_PASSWORD = os.getenv("PROCESS_PASSWORD")

# Define log directory and file prefix
log_dir = "./Log/Bowser_Logging"
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

# Setup logging for the application
log_dir = "./Log/Bowser_Logging"
setup_logging(log_dir)


@app.route('/Bowser', methods=['POST'])
def bowser():
    """
    Endpoint to receive messages and execute corresponding scripts.
    """
    # Extract data from request
    json_master_password = request.json.get('master_password')
    json_process_password = request.json.get('process_password')
    json_process_name = request.json.get('process_name')

    # Validate inputs
    if not all([json_master_password, json_process_password, json_process_name]):
        app.logger.error("Invalid input")
        abort(400)  # Bad Request

    # Check for unauthorized access
    if json_master_password != MASTER_PASSWORD or json_process_password != PROCESS_PASSWORD:
        app.logger.error("Unauthorized access attempt")
        abort(401)  # Unauthorized

    # Receive message from request and sanitize it
    message = html.escape(request.json.get('message'))
    app.logger.info(f"Received message: {message} for process: {json_process_name}")

    # Execute the appropriate script based on process name
    try:
        subprocess.run(['python', f'./PyRocesses/API-Triggered/Enabled/{json_process_name}/{json_process_name}.py', message], check=True)
        app.logger.info(f"Process completed successfully: {json_process_name}.py")
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Failed to execute {json_process_name}.py: {e}")
        return f"Failed to execute {json_process_name}.py: {e}", 500

    return f"Message received and processed by {json_process_name}", 200


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)