import RPi.GPIO as GPIO
import time
import urllib2
import json
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(21,GPIO.IN)

def sendNotification(token, channel, message):
    data = {
            "body" : message,
            "message_type" : "text/plain"
    }

    req = urllib2.Request('http://api.pushetta.com/api/pushes/{0}/'.format(channel))
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', 'Token {0}'.format(token))

    response = urllib2.urlopen(req, json.dumps(data))

while True:
	input_state = GPIO.input(21)
	if input_state == True:
		GPIO.output(10,1)
		print('Detektovan pokret')
                sendNotification("65a2b274210c698c17f91b1bb8a7b1ae6e886ca", "Jovica_RaspberryPi", "Detektovan pokret")
		time.sleep(2)
                GPIO.output(10,0)
                time.sleep(2)
