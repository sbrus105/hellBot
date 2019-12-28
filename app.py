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



def webhook(): #message analysis logic should go here, not familiar with python, so I'm not certain if data is kept from call to call
  data = request.get_json()
  log('Received {}'.format(data))

  if data['name'] != 'hellBot':#not message from self

    if "OU" in data['text']:                                                                 #OU
        msg = "OU sux!"
        send_message(msg)

    if re.search('420', data['text'], re.IGNORECASE):                                                                      #420
        msg = "Blaze it"
        send_message(msg)

    if re.search(' 69 ', data['text'], re.IGNORECASE):                                                                      #69
        msg = "Nice."
        send_message(msg)

    if re.search('tequila', data['text'], re.IGNORECASE):
        msg = "If you're going to drink tequila, at least make it good tequila."                                            #tequila
        send_message(msg)

    if re.search('everclear', data['text'], re.IGNORECASE):
        msg = "Nothing good ever came out of a night that involved Everclear, remember that."                               #everclear
        send_message(msg)

    if re.search('!sam', data['text'], re.IGNORECASE):
        msg = "712 Graham Place, apt 303, Austin TX 78705. Looks like a motel"                                              #!sam
        send_message(msg)

    if re.search('!tailgate', data['text'], re.IGNORECASE):
        msg = "Orange Tree Condos, across Rio Grande from Graham Place."                                                    #!tailgate
        send_message(msg)

    if re.search('!hellBot', data['text'], re.IGNORECASE):
        msg = "Hello, I am a GroupMe chat bot developed by Sam Brus and Harrison Berrier. Please keep in mind that Sam is unfamiliar with the" \
              " bastard language known as Python so development will be slow and somewhat buggy."                          #!hellBot
        send_message(msg)

    if re.search('!schedule', data['text'], re.IGNORECASE):                                                                #!schedule
        msg = "WIP"
        send_message(msg)

    if re.search('Sigma Pi', data['text'], re.IGNORECASE):                                                               #Sigma Pi
        msg = "ROLL PI BABY!"
        send_message(msg)

    if re.search('Boogachiga boogachiga', data['text'], re.IGNORECASE):                                                  #boogachiga
        msg = "FDH!"
        send_message(msg)

    if re.search('FDH FDH', data['text'], re.IGNORECASE):                                                                #FDH
        msg = "F!D!H!"
        send_message(msg)

    if re.search('Baylor', data['text'], re.IGNORECASE):                                                                 #baylor
        msg = "2 - 4 - 6 - 8 - 10, Baylor Women look like men!"
        send_message(msg)

    if re.search('aggie', data['text'], re.IGNORECASE):                                                                  #aggie
        msg = "Sheep Fuckers"
        send_message(msg)

    if re.search('A&M', data['text'], re.IGNORECASE):                                                                    #A&M
        msg = "Sheep Fuckers"
        send_message(msg)

    if re.search('TAMU', data['text'], re.IGNORECASE):                                                                   #TAMU
        msg = "Sheep Fuckers"
        send_message(msg)

    if re.search('removed Sam Brus from the group.', data['text'], re.IGNORECASE):                                       #Try me
        msg = "You're a huge bitch for that"
        send_message(msg)

    if re.search('added Sam Brus to the group.', data['text'], re.IGNORECASE):                                           #Try me
        msg = "Shoutout for being a real one \m/"
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
