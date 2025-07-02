# bot.py
import requests
import time

BOT_TOKEN = 'your_bot_token_here'
CHAT_ID = 'your_chat_id_here'
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
    time.sleep(3600)  # 1 hour
