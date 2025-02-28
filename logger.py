import logging
import os
import time
import json

LOG_DIR = "/var/log/security_automation"
LOG_FILE = os.path.join(LOG_DIR, "automation_log.json")

logging.basicConfig(filemode="error_logs.txt", level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def log_error(event, details, alert=False):
    error_data = {
        "timestamp": time.time(),
        "event": event,
        "details":"An internal error occured."
    }

    # Write error to log file in JSON format
    with open(LOG_FILE, "a") as file:
        file.write(json.dumps(error_data) + "\n")

    logging.error(f"{event}: {details}")


""" def run_log(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CallProcessError as e:
        log_error("Task Failed", f"Command: {command}, Error {e}", alert=True ) """