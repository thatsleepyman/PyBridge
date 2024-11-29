# Import Modules
import os
import subprocess
from flask import Flask, request, abort
import html
import json


# Initialize Flask app
app = Flask(__name__)


# Get the relative path to the Python interpreter
python_path = os.path.join(
    os.getcwd()
    , '..'
    , '..'
    , 'PyBridge'
    , '.venv'
    , 'Scripts'
    , 'python.exe')


# Main routing
@app.route('/PyBridge/main/<string:PYROCESS_NAME>', methods=['POST'])
def PyBridge_main(PYROCESS_NAME):
    # Load tokens from the JSON file
    tokens_json_path = os.path.join(
        os.getcwd()
        , '..'
        , '..'
        , 'PyBridge'
        , 'config'
        , 'tokens_main.json')

    with open(tokens_json_path) as f:
        tokens = json.load(f)

    MASTER_TOKEN = tokens['MASTER_TOKEN']
    USER_TOKEN = tokens['USER_TOKEN']
    PYROCESS_TOKENS = tokens['PYROCESS_TOKENS_MAIN']

    # Extract data from request
    json_MASTER_TOKEN = request.json.get('MASTER_TOKEN')
    json_USER_TOKEN = request.json.get('USER_TOKEN')
    json_PYROCESS_TOKEN = request.json.get('PYROCESS_TOKEN')

    # Validate inputs
    if not all([json_MASTER_TOKEN
                , json_USER_TOKEN
                , json_PYROCESS_TOKEN]):
        app.logger.error("Invalid input")
        abort(400)  # Bad Request

    # Check for unauthorized access
    if (json_MASTER_TOKEN != MASTER_TOKEN
            or json_USER_TOKEN != USER_TOKEN
            or json_PYROCESS_TOKEN != PYROCESS_TOKENS[PYROCESS_NAME]):
        app.logger.error("Unauthorized access attempt")
        abort(401)  # Unauthorized

    # Receive message from request and sanitize it
    html_san_MESSAGE = html.escape(request.json.get('json_MESSAGE'))
    app.logger.info(f"Received message: {html_san_MESSAGE} for PyRocess: {PYROCESS_NAME}")

    # Execute the appropriate script based on pyrocess name
    try:
        script_path = os.path.join(
            os.getcwd()
            , '..'
            , '..'
            , 'PyBridge'
            , 'src'
            , 'PyRocesses'
            , 'API-Triggered'
            , 'main'
            , PYROCESS_NAME
            , f'{PYROCESS_NAME}.py')

        subprocess.run([python_path, script_path, html_san_MESSAGE], check=True)
        app.logger.info(f"PyRocess triggered successfully: {PYROCESS_NAME}.py")
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Failed to trigger {PYROCESS_NAME}.py: {e}")
        return f"Failed to trigger {PYROCESS_NAME}.py: {e}", 500

    return f"Message received and triggered {PYROCESS_NAME}", 200


# Developer routing
@app.route('/PyBridge/dev/<string:PYROCESS_NAME>', methods=['POST'])
def PyBridge_dev(PYROCESS_NAME):
    # Load tokens from the JSON file
    tokens_json_path = os.path.join(
        os.getcwd()
        , '..'
        , '..'
        , 'PyBridge'
        , 'config'
        , 'tokens_dev.json')

    with open(tokens_json_path) as f:
        tokens = json.load(f)

    MASTER_TOKEN = tokens['MASTER_TOKEN']
    DEVELOPER_TOKEN = tokens['DEVELOPER_TOKEN']
    PYROCESS_TOKENS = tokens['PYROCESS_TOKENS_DEV']

    # Extract data from request
    json_MASTER_TOKEN = request.json.get('MASTER_TOKEN')
    json_DEVELOPER_TOKEN = request.json.get('DEVELOPER_TOKEN')
    json_PYROCESS_TOKEN = request.json.get('PYROCESS_TOKEN')

    # Validate inputs
    if not all([json_MASTER_TOKEN
                , json_DEVELOPER_TOKEN
                , json_PYROCESS_TOKEN]):
        app.logger.error("Invalid input")
        abort(400)  # Bad Request

    # Check for unauthorized access
    if (json_MASTER_TOKEN != MASTER_TOKEN
            or json_DEVELOPER_TOKEN != DEVELOPER_TOKEN
            or json_PYROCESS_TOKEN != PYROCESS_TOKENS[PYROCESS_NAME]):
        app.logger.error("Unauthorized access attempt")
        abort(401)  # Unauthorized

    # Receive message from request and sanitize it
    html_san_MESSAGE = html.escape(request.json.get('json_MESSAGE'))
    app.logger.info(f"Received message: {html_san_MESSAGE} for PyRocess: {PYROCESS_NAME}")

    # Execute the appropriate script based on pyrocess name
    try:
        script_path = os.path.join(
            os.getcwd()
            , '..'
            , '..'
            , 'PyBridge'
            , 'src'
            , 'PyRocesses'
            , 'API-Triggered'
            , 'dev'
            , PYROCESS_NAME
            , f'{PYROCESS_NAME}.py')

        subprocess.run([python_path, script_path, html_san_MESSAGE], check=True)
        app.logger.info(f"PyRocess triggered successfully: {PYROCESS_NAME}.py")
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Failed to trigger {PYROCESS_NAME}.py: {e}")
        return f"Failed to trigger {PYROCESS_NAME}.py: {e}", 500

    return f"Message received and triggered {PYROCESS_NAME}", 200


# test routing
@app.route('/PyBridge/test/<string:PYROCESS_NAME>', methods=['POST'])
def PyBridge_test(PYROCESS_NAME):
    # Load tokens from the JSON file
    tokens_json_path = os.path.join(
        os.getcwd()
        , '..'
        , '..'
        , 'PyBridge'
        , 'config'
        , 'tokens_test.json')

    with open(tokens_json_path) as f:
        tokens = json.load(f)

    MASTER_TOKEN = tokens['MASTER_TOKEN']
    TESTER_TOKEN = tokens['TESTER_TOKEN']
    PYROCESS_TOKENS = tokens['PYROCESS_TOKENS_TEST']

    # Extract data from request
    json_MASTER_TOKEN = request.json.get('MASTER_TOKEN')
    json_TESTER_TOKEN = request.json.get('TESTER_TOKEN')
    json_PYROCESS_TOKEN = request.json.get('PYROCESS_TOKEN')

    # Validate inputs
    if not all([json_MASTER_TOKEN
                , json_TESTER_TOKEN
                , json_PYROCESS_TOKEN]):
        app.logger.error("Invalid input")
        abort(400)  # Bad Request

    # Check for unauthorized access
    if (json_MASTER_TOKEN != MASTER_TOKEN
            or json_TESTER_TOKEN != TESTER_TOKEN
            or json_PYROCESS_TOKEN != PYROCESS_TOKENS[PYROCESS_NAME]):
        app.logger.error("Unauthorized access attempt")
        abort(401)  # Unauthorized

    # Receive message from request and sanitize it
    html_san_MESSAGE = html.escape(request.json.get('json_MESSAGE'))
    app.logger.info(f"Received message: {html_san_MESSAGE} for PyRocess: {PYROCESS_NAME}")

    # Execute the appropriate script based on pyrocess name
    try:
        script_path = os.path.join(
            os.getcwd()
            , '..'
            , '..'
            , 'PyBridge'
            , 'src'
            , 'PyRocesses'
            , 'API-Triggered'
            , 'test'
            , PYROCESS_NAME
            , f'{PYROCESS_NAME}.py')

        subprocess.run([python_path, script_path, html_san_MESSAGE], check=True)
        app.logger.info(f"PyRocess triggered successfully: {PYROCESS_NAME}.py")
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Failed to trigger {PYROCESS_NAME}.py: {e}")
        return f"Failed to trigger {PYROCESS_NAME}.py: {e}", 500

    return f"Message received and triggered {PYROCESS_NAME}", 200


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=False)
