import os
import sys
import json
import re
import random
import time

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

    if re.search('tequila', data['text'], re.IGNORECASE):
        msg = "If you're going to drink tequila, at least make it good tequila."
        send_message(msg)

    if re.search('everclear', data['text'], re.IGNORECASE):
        msg = "Nothing good ever came out of a night that involved Everclear, remember that."
        send_message(msg)

    if re.search('!sam', data['text'], re.IGNORECASE):
        msg = "712 Graham Place, apt 303, Austin TX 78705. Looks like a motel"
        send_message(msg)

    if re.search('!tailgate', data['text'], re.IGNORECASE):
        msg = "Orange Tree Condos, across Rio Grande from Graham Place."
        send_message(msg)

    if re.search('!hellBot', data['text'], re.IGNORECASE):
        msg = "Hello, I am a GroupMe chat bot developed by Sam Brus. Please keep in mind that Sam is unfamiliar with the" \
              "bastard language known as Python so development will be slow and somewhat buggy."
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
