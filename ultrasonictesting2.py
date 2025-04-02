import RPi.GPIO as GPIO
import time
from datetime import datetime
try:
    GPIO.setmode(GPIO.BCM)
    TRIG = 23
    ECHO = 24
    print("DISTANCE MESURE IN PROGRES..")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)
    print("Waiting for sensor :)")
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00005)
    GPIO.output(TRIG,False)
#    print("astallafa")
    while GPIO.input(ECHO) == 0:
#        print("0000")
        pulse_start = time.time()
    while GPIO.input(ECHO)== 1:
#        print("1111m")
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance,2)
    print(f"Distance: {distance} CM")
    today = datetime.now()
    todaydate = today.date()
    todaytime = today.time()
    print(f"{todaydate} {todaytime}")
    with open("distance.txt", 'a') as file:
        today = datetime.now()
        file.write(f"Distance: {distance} CM. {today.date()} {today.time()} \n")
#    GPIO.cleanup()
except KeyboardInterrupt:
    print("interrupted.....")
except:
    print("idk")
finally:
    GPIO.cleanup()
