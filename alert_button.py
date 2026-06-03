import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False

while True:
    button_state = GPIO.input(7)

    if button_state == GPIO.HIGH and button_pressed == False:
        print("Someone pressed the alert button!")
        button_pressed = True
        time.sleep(0.5)

    if button_state == GPIO.LOW:
        button_pressed = False

    time.sleep(0.1)
