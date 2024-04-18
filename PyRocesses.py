import os
import logging
import shutil

root_path = os.path.dirname(os.path.abspath(__file__))

def get_directories_with_status(path):
    path = os.path.join(root_path, path)  
    directories = {}
    for dir_name in os.listdir(path):
        abs_path = os.path.join(path, dir_name)
        status = "enabled" if "Enabled" in path else "disabled"
        directories[dir_name] = status
    return directories

def get_script_directories():
    enabled_path = 'PyRocesses\\Enabled'
    disabled_path = 'PyRocesses\\Disabled'
    
    enabled_dirs = get_directories_with_status(enabled_path)
    disabled_dirs = get_directories_with_status(disabled_path)
    return enabled_dirs, disabled_dirs

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
    
    source_dir = enabled_path if new_status == "disabled" else disabled_path
    
    try:
        logging.info(f"Moving script folder {script_name} from {source_dir} to {script_path}")
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

def toggle_script(script_name):
    current_status = get_script_status(script_name)
    new_status = "disabled" if current_status == "enabled" else "enabled"
    success = move_script_folder(script_name, new_status)
    if success:
        return new_status
    else:
        return current_status