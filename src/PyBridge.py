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

# Get master, pyrocess and developer Tokens
MASTER_TOKEN = os.getenv("MASTER_TOKEN")
PYROCESS_TOKEN = os.getenv("PYROCESS_TOKEN")
DEVELOPER_TOKEN = os.getenv("DEVELOPER_TOKEN")

# Get the relative path to the Python interpreter
python_path = os.path.join(os.getcwd(), '..', '..', 'PyBridge', '.venv', 'Scripts', 'python.exe')


# Main routing
@app.route('/PyBridge', methods=['POST'])
def PyBridge():
    # Extract data from request
    json_MASTER_TOKEN = request.json.get('MASTER_TOKEN')
    json_PYROCESS_TOKEN = request.json.get('PYROCESS_TOKEN')
    json_PYROCESS_NAME = request.json.get('PYROCESS_NAME')

    # Validate inputs
    if not all([json_MASTER_TOKEN
                , json_PYROCESS_TOKEN
                , json_PYROCESS_NAME]):
        app.logger.error("Invalid input")
        abort(400)  # Bad Request

    # Check for unauthorized access
    if (json_MASTER_TOKEN != MASTER_TOKEN
            or json_PYROCESS_TOKEN != PYROCESS_TOKEN):
        app.logger.error("Unauthorized access attempt")
        abort(401)  # Unauthorized

    # Receive message from request and sanitize it
    html_san_MESSAGE = html.escape(request.json.get('json_MESSAGE'))
    app.logger.info(f"Received message: {html_san_MESSAGE} for PyRocess: {json_PYROCESS_NAME}")

    # Execute the appropriate script based on pyrocess name
    try:
        script_path = os.path.join(os.getcwd(), '..', '..', 'PyBridge', 'src', 'PyRocesses', 'API-Triggered', 'Enabled',
                                   json_PYROCESS_NAME, f'{json_PYROCESS_NAME}.py')
        subprocess.run([python_path, script_path, html_san_MESSAGE], check=True)
        app.logger.info(f"PyRocess triggered successfully: {json_PYROCESS_NAME}.py")
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Failed to trigger {json_PYROCESS_NAME}.py: {e}")
        return f"Failed to trigger {json_PYROCESS_NAME}.py: {e}", 500

    return f"Message received and triggered {json_PYROCESS_NAME}", 200


# Developer routing
@app.route('/PyBridge_dev', methods=['POST'])
def PyBridge_dev():
    # Extract data from request
    json_MASTER_TOKEN = request.json.get('MASTER_TOKEN')
    json_DEVELOPER_TOKEN = request.json.get('DEVELOPER_TOKEN')
    json_PYROCESS_TOKEN = request.json.get('PYROCESS_TOKEN')
    json_PYROCESS_NAME = request.json.get('PYROCESS_NAME')

    # Validate inputs
    if not all([json_MASTER_TOKEN, json_DEVELOPER_TOKEN
                , json_PYROCESS_TOKEN
                , json_PYROCESS_NAME]):
        app.logger.error("Invalid input, check tokens or PyRocess name")
        abort(400)  # Bad Request

    # Check for unauthorized access
    if (json_MASTER_TOKEN != MASTER_TOKEN
            or json_DEVELOPER_TOKEN != DEVELOPER_TOKEN
            or json_PYROCESS_TOKEN != PYROCESS_TOKEN):
        app.logger.error("Unauthorized access attempt")
        abort(401)  # Unauthorized

    # Receive message from request and sanitize it
    html_san_MESSAGE = html.escape(request.json.get('json_MESSAGE'))
    app.logger.info(f"Received message: {html_san_MESSAGE} for PyRocess: {json_PYROCESS_NAME}")

    # Execute the appropriate script based on pyrocess name
    try:
        script_path = os.path.join(os.getcwd(), '..', '..', 'PyBridge', 'src', 'PyRocesses', 'API-Triggered',
                                   'Developer_Tools', json_PYROCESS_NAME, f'{json_PYROCESS_NAME}.py')
        subprocess.run([python_path, script_path, html_san_MESSAGE], check=True)
        app.logger.info(f"PyRocess triggered successfully: {json_PYROCESS_NAME}.py")
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Failed to trigger {json_PYROCESS_NAME}.py: {e}")
        return f"Failed to trigger {json_PYROCESS_NAME}.py: {e}", 500

    return f"Message received and triggered {json_PYROCESS_NAME}", 200


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
