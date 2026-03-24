import time
import RPi.GPIO as GPIO

PIR_pin = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_pin, GPIO.IN)

print("Motion Detection Started")

try:
    while True:
        if GPIO.input(PIR_pin):
            print("Motion detected!")
        else:
            print("No motion detected.")
        time.sleep(1)

except KeyboardInterrupt:
    print("Program interrupted by user.")

finally:
    GPIO.cleanup()
