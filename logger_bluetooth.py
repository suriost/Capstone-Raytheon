import serial
import time
from datetime import datetime

# === CONFIGURATION ===
SERIAL_PORT = '/dev/rfcomm0 '  # For Bluetooth Connection
BAUD_RATE = 9600
LOG_FILE = '/home/pi/arduino_data.log'

# === HELPER FUNCTION ===
def parse_and_log(line):
    timestamp = datetime.now().isoformat()
    parts = line.strip().split(' ', 1)
    
    if len(parts) < 2:
        print(f"[WARN] Invalid data: {line}")
        return
    
    keyword, content = parts
    with open(LOG_FILE, 'a') as f:
        f.write(f"{timestamp} [{keyword}] {content}\n")
    
    print(f"Received [{keyword}]: {content}")

# === MAIN LOOP ===
def listen_serial():
    print(f"Connecting to {SERIAL_PORT} at {BAUD_RATE} baud...")
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            print("Connected. Waiting for data...")
            while True:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').strip()
                    if line:
                        parse_and_log(line)
                time.sleep(0.1)
    except serial.SerialException as e:
        print(f"[ERROR] Could not open serial port: {e}")

if __name__ == '__main__':
    listen_serial()






# import logging
# import os
# import time
# import json

# LOG_DIR = "/var/log/security_automation"
# LOG_FILE = os.path.join(LOG_DIR, "automation_log.json")

# logging.basicConfig(filemode="error_logs.txt", level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# def log_error(event, details, alert=False):
#     error_data = {
#         "timestamp": time.time(),
#         "event": event,
#         "details":"An internal error occured."
#     }

#     # Write error to log file in JSON format
#     with open(LOG_FILE, "a") as file:
#         file.write(json.dumps(error_data) + "\n")

#     logging.error(f"{event}: {details}")


# """ def run_log(command):
#     try:
#         result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
#         return result.stdout
#     except subprocess.CallProcessError as e:
#         log_error("Task Failed", f"Command: {command}, Error {e}", alert=True ) """