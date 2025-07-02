import requests
import time
import os

BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']
MESSAGE = 'I love you ❤️'

def send_message():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': MESSAGE}
    try:
        requests.post(url, data=payload)
        print("Message sent.")
    except Exception as e:
        print(f"Error: {e}")

while True:
    send_message()
    time.sleep(3600)
