import os
import datetime
import logging
from flask import Flask, render_template, request, jsonify
from PyRocesses import get_script_directories, toggle_script

# Set the root path to the directory containing the Python script
root_path = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, root_path=root_path)

# Configure logging
log_folder = os.path.join(root_path, 'Logs\\Bowser_Logs')
os.makedirs(log_folder, exist_ok=True)
log_file_name = os.path.join(log_folder, f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{app.name}.log")
logging.basicConfig(filename=log_file_name, level=logging.INFO, format='%(asctime)s %(levelname)s in %(name)s: %(message)s')

# Route to display the list of scripts
@app.route('/')
def index():
    # Log the request
    log_request(request)
    
    directories = {}
    enabled_dirs, disabled_dirs = get_script_directories()
    directories.update(enabled_dirs)
    directories.update(disabled_dirs)
    logging.info('Displayed directory list')
    return render_template('index.html', directories=directories)

# Route to toggle the status of a script
@app.route('/toggle/<script_name>', methods=['POST'])
def toggle(script_name):
    new_status = toggle_script(script_name)
    return new_status

# Function to log the request
def log_request(req):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ip_address = req.remote_addr
    http_method = req.method
    url = req.url
    status_code = 200  # Assuming success by default
    user_agent = req.user_agent.string
    log_entry = f"[{timestamp}] {ip_address} - {http_method} {url} - {status_code} - {user_agent}\n"
    logging.info(log_entry)


if __name__ == '__main__':
    app.run(debug=True)