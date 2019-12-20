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
  if data['name'] != 'briskeybot':                       #not message from self
    if re.search('gbq', data['text'], re.IGNORECASE):    #It's Jacob If                #The meat
        msg = "It's Jacob."
        send_message(msg)

  return "ok", 200  #send all applicable messages



def send_message(msg):
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
