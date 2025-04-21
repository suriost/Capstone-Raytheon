import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import datetime
import csv

# --- Sensor Pin Definitions ---
DHT_PIN = 4
DHT_SENSOR = Adafruit_DHT.DHT11
TRIG_PIN = 23
ECHO_PIN = 24

# --- GPIO Setup ---
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# --- Functions for Sensor Readings ---
def get_distance():
    """Measures the distance using the ultrasonic sensor."""
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        StartTime = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance_cm = (TimeElapsed * 34300) / 2
    return distance_cm

def get_temperature_humidity():
    """Reads temperature and humidity from the DHT11 sensor."""
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return temperature, humidity
    else:
        print("Failed to get DHT reading.")
        return None, None

# --- CSV Storage Configuration ---
CSV_FILE = "sensor_data.csv"
CSV_HEADER = ["timestamp", "temperature_c", "humidity_percent", "distance_cm"]

def write_to_csv(data):
    """Writes a list of data to the CSV file."""
    with open(CSV_FILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:  # Write header only if the file is new/empty
            writer.writerow(CSV_HEADER)
        writer.writerow(data)

if __name__ == "__main__":
    try:
        while True:
            now = datetime.datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

            temperature, humidity = get_temperature_humidity()
            distance = get_distance()

            if temperature is not None and humidity is not None:
                data_to_write = [timestamp, f"{temperature:.2f}", f"{humidity:.2f}", f"{distance:.2f}"]
                write_to_csv(data_to_write)
                print(f"Data written: {data_to_write}")

            time.sleep(5)  # Adjust the data logging interval as needed

    except KeyboardInterrupt:
        print("Data logging stopped by user.")
    finally:
        GPIO.cleanup()