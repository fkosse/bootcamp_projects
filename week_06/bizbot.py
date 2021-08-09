import pyjokes
import requests
import time

webhook_url = ""

joke = pyjokes.get_joke()

data = {'text': joke}

while True:
    time.sleep(30)
    requests.post(url=webhook_url, json = data)