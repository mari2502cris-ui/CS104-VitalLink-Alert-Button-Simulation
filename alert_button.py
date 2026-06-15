import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

BOT_TOKEN = "8971769762:AAGsTOLDfP7rib-cNrJDvhIPPzE-ehWNRMw"
CHAT_ID = "8919040298"

def send_alert():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": "Someone pressed the alert button!"
    }
    response = requests.post(url, json=data)
    print(response.text)

button_pressed = False

while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone pressed the alert button!")
        send_alert()
        button_pressed = True
        time.sleep(0.5)

    if GPIO.input(7) == GPIO.LOW:
        button_pressed = False
