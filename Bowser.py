import os
import datetime
import logging
from flask import Flask, render_template, request, jsonify
import shutil

# Set the root path to the directory containing the Python script
root_path = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, root_path=root_path)

# Configure logging
log_folder = os.path.join(root_path, 'Logs\\Bowser_Logs')
os.makedirs(log_folder, exist_ok=True)
log_file_name = os.path.join(log_folder, f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{app.name}.log")
logging.basicConfig(filename=log_file_name, level=logging.INFO, format='%(asctime)s %(levelname)s in %(name)s: %(message)s')

# Function to get the list of directories under a given path with their statuses
def get_directories_with_status(path):
    path = os.path.join(root_path, path)  # Construct absolute path relative to root_path
    directories = {}
    for dir_name in os.listdir(path):
        abs_path = os.path.join(path, dir_name)
        status = "enabled" if "Enabled" in path else "disabled"
        directories[dir_name] = status
    return directories

# Function to get the list of directories under Enabled and Disabled folders
def get_script_directories():
    enabled_path = 'PyRocesses\\Enabled'
    disabled_path = 'PyRocesses\\Disabled'
    
    enabled_dirs = get_directories_with_status(enabled_path)
    disabled_dirs = get_directories_with_status(disabled_path)
    return enabled_dirs, disabled_dirs

# Helper function to get the current status of a script
def get_script_status(script_name):
    enabled_path = os.path.join(root_path, 'PyRocesses\\Enabled')
    disabled_path = os.path.join(root_path, 'PyRocesses\\Disabled')
    
    if os.path.exists(os.path.join(enabled_path, script_name)):
        return "enabled"
    elif os.path.exists(os.path.join(disabled_path, script_name)):
        return "disabled"
    else:
        return None

def move_script_folder(script_name, new_status):
    enabled_path = os.path.join(root_path, 'PyRocesses\\Enabled')
    disabled_path = os.path.join(root_path, 'PyRocesses\\Disabled')
    script_path = os.path.join(root_path, f'PyRocesses\\{new_status.capitalize()}', script_name)
    
    # Determine the source directory based on the current status
    source_dir = enabled_path if new_status == "disabled" else disabled_path
    
    try:
        logging.info(f"Moving script folder {script_name} from {source_dir} to {script_path}")
        # Log source and destination paths
        logging.info(f"Source path: {os.path.join(source_dir, script_name)}")
        logging.info(f"Destination path: {script_path}")
        shutil.move(os.path.join(source_dir, script_name), script_path)
        return True
    except FileNotFoundError as e:
        logging.error(f"File not found error: {e}")
    except PermissionError as e:
        logging.error(f"Permission error: {e}")
    except Exception as e:
        logging.error(f"Error moving script folder: {e}")
    return False

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
def toggle_script(script_name):
    # Get the current status of the script
    current_status = get_script_status(script_name)
    
    # Toggle the status of the script
    new_status = "disabled" if current_status == "enabled" else "enabled"
    
    # Move the script folder to the corresponding directory
    success = move_script_folder(script_name, new_status)
    
    # Change the text displaying the current status in the GUI
    if success:
        return new_status
    else:
        return current_status

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
