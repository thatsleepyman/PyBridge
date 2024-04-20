import os
import logging
from datetime import datetime

def setup_logging(log_dir, log_file_prefix):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = f"{log_dir}/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{log_file_prefix}.log"
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')