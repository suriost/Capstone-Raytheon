import subprocess
import hashlib
import logging

# Configuration
# TODO: Hash Arduino firmware to save into TRUSTED_HASH
# TODO: Run avrdude -p ? on PI to find ARDUINO_TYPE
ARDUINO_TYPE = ""  
PORT = "/dev/ttyUSB0"        
TRUSTED_HASH = ""  

# Setup logging
logging.basicConfig(filename='integrity.log', level=logging.INFO)

def read_arduino_firmware():
    """Use avrdude to dump Arduino flash memory into a binary file."""
    try:
        cmd = [
            "avrdude",
            "-p", ARDUINO_TYPE,
            "-c", "arduino",
            "-P", PORT,
            "-U", "flash:r:firmware_dump.bin:r",
            "-q", "-q"  
        ]
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to read firmware: {e}")
        return False


# TODO: 
def compute_sha256(file_path):
    """Compute SHA-256 hash of a file"""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

def verify_firmware():
    """Main verification logic"""
    if not read_arduino_firmware():
        return False
    
    # TODO: Find firmware path for Arduino
    current_hash = compute_sha256("firmware_dump.bin")
    logging.info(f"Current firmware hash: {current_hash}")
    logging.info(f"Trusted firmware hash: {TRUSTED_HASH}")

    if current_hash == TRUSTED_HASH:
        logging.info("Firmware integrity verified!")
        return True
    else:
        logging.error("Firmware integrity FAILED!")
        return False

if __name__ == "__main__":
    if verify_firmware():
        print("Firmware OK.")
    else:
        print("Firmware compromised!")