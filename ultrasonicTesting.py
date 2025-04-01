import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
TRIG = 23  # GPIO pin for Trigger
ECHO = 24  # GPIO pin for Echo

print("Distance Measurement In Progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("Waiting For Sensor To Settle")
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.0001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
    pulse_start = time.time()

while GPIO.input(ECHO)==1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print(f"Distance: {distance} cm")

GPIO.cleanup()
