import os
import sys
import json
import re
import random

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__) #dont touch
@app.route('/', methods=['POST'])



def webhook():
  data = request.get_json()
  log('Received {}'.format(data))
  if data['name'] != 'hellBot':                       #not message from self

    if re.search('OU sucks', data['text'], re.IGNORECASE):
        msg = "OU sux!"
        send_message(msg)

    if re.search('OU sux', data['text'], re.IGNORECASE): 
        msg = "OU sux!"
        send_message(msg)

    if re.search('420', data['text'], re.IGNORECASE):    
        msg = "Blaze it"
        send_message(msg)

    if re.search(' 69 ', data['text'], re.IGNORECASE):
        msg = "Nice."
        send_message(msg)


  return "ok", 200  #send all applicable messages



def send_message(msg):
    from time import sleep
    sleep(0.05)
    url  = 'https://api.groupme.com/v3/bots/post'
  
    #f841583c50c73aa774df650ffd  	LHH Chat
    #44730fb274b2b3538d071f6f84		Tester NOT CONFIGURED YET
    data = {
        'bot_id' : 'f841583c50c73aa774df650ffd', #replace this code with above ones for corresponding GM
        'text'   : msg,
       }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()



def log(msg):
  print(str(msg))
  sys.stdout.flush()
