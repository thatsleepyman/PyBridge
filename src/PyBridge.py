# Standard library imports
import os
import subprocess

# Third-party imports
from flask import Flask, request, abort
import html
from dotenv import load_dotenv


# Initialize Flask app
app = Flask(__name__)
load_dotenv()


# Get master, process and developer Tokens
MASTER_TOKEN = os.getenv("MASTER_TOKEN")
PROCESS_TOKEN = os.getenv("PROCESS_TOKEN")
DEVELOPER_TOKEN = os.getenv("DEVELOPER_TOKEN")


# Get the relative path to the Python interpreter
python_path = os.path.join(os.getcwd(), '..', '..', 'PyBridge', '.venv', 'Scripts', 'python.exe')


# Main routing
@app.route('/PyBridge', methods=['POST'])
def PyBridge():
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
        script_path = os.path.join(os.getcwd(), '..', '..', 'PyBridge', 'src', 'PyRocesses', 'API-Triggered', 'Enabled', json_process_name, f'{json_process_name}.py')
        subprocess.run([python_path, script_path, message], check=True)
        app.logger.info(f"Process triggered successfully: {json_process_name}.py")
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Failed to trigger {json_process_name}.py: {e}")
        return f"Failed to trigger {json_process_name}.py: {e}", 500

    return f"Message received and triggered {json_process_name}", 200


# Developer routing
@app.route('/PyBridge_dev', methods=['POST'])
def PyBridge_dev():
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
        script_path = os.path.join(os.getcwd(), '..', '..', 'PyBridge', 'src', 'PyRocesses', 'API-Triggered', 'Developer_Tools', json_process_name, f'{json_process_name}.py')
        subprocess.run([python_path, script_path, message], check=True)
        app.logger.info(f"Process triggered successfully: {json_process_name}.py")
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Failed to trigger {json_process_name}.py: {e}")
        return f"Failed to trigger {json_process_name}.py: {e}", 500

    return f"Message received and triggered {json_process_name}", 200


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
