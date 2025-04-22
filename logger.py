import serial
import time
from datetime import datetime
import os
import csv

# * * * * * CONFIGURATION * * * * * 
SERIAL_PORT = '/dev/ttyUSB0'  # For wired connection
BAUD_RATE = 9600
BASE_DIR = '/home/pi/arduino_logs'

# * * * * * Log to respective file * * * * 
def log_data(keyword, content):
    timestamp = datetime.now().isoformat()  # Saves timestamp of log
    
    # Save log to respective file based on keyword
    # TODO: ADD INFO VERIFICAITON FUNCTIONS/PROGRAMS FOR ERROR MESSAGES 
    keyword_upper = keyword.upper()         
    match keyword_upper:    # Finds filename
        case 'HASH':
            file_name = 'hashes.csv'
        case 'ULTRASENSOR':
            file_name = 'ultrasensor.csv'
        # TODO: Change based on other sensor names
        case 'SENSOR':
            file_name = 'sensors.csv'
        case _:
            file_name = 'unknown.csv'

    file_path = os.path.join(BASE_DIR, file_name)   # Creates fullpath to file      EX: '/home/pi/arduino_logs/hashes.csv'
    file_exists = os.path.isfile(file_path)         # Checks if file exists already

    with open(file_path, 'a', newline='') as csvfile:   # Adds to or creates file 
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(['timestamp', 'data'])  # Creates header
        writer.writerow([timestamp, content])       # Saves content to file
    
    print(f"Saved to {file_path}: {timestamp}, {content}")  # Checker output

# * * * * * Parse and Formats Log Line * * * * * 
def parse_and_log(line):
    parts = line.strip().split(' ', 1)
    
    # ******** FIXME: CHANGE BASED ON OUTPUTS OR REMOVE **********
    if len(parts) < 2:
        print(f"[WARN] Invalid data: {line}")
        return
    
    keyword, content = parts
    log_data(keyword, content)


# * * * * * Main Loop * * * * * 
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
