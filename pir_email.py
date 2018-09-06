import RPi.GPIO as GPIO
import time

sensor = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

while True:
        i=0
        time.sleep(0.01)
        previous_state = current_state
        current_state = GPIO.input(sensor)
        if current_state != previous_state:
            while i<5 and current_state:              
                GPIO.output(10,1)
                time.sleep(0.2)
                GPIO.output(10,0)
                time.sleep(0.2)
                i+=1
            new_state = "HIGH" if current_state else "LOW"
            print("GPIO pin %s is %s" % (sensor, new_state))
            import smtplib
            if new_state == "HIGH":                  
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login("email adresa", "password")
             
                msg = "Detektovan pokret!!!"
                server.sendmail("sa adrese", "na adresu", msg)
                server.quit()
                
