import argparse
import RPi.GPIO as GPIO
import time
# make_server is used to create this simple python webserver
from wsgiref.simple_server import make_server


parser = argparse.ArgumentParser(description='Blinking LED')

parser.add_argument('blink')


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)



# Function that is ran when a http request comes in
def simple_app(env, start_response):

    # set some http headers that are sent to the browser
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)

    # What did the user ask for?
    if env["PATH_INFO"] == "/on":
        print("user asked for /on")
	GPIO.output(18,GPIO.HIGH)
        return "got on"
    elif env["PATH_INFO"] == "/off":
        print("user asked for /off")
	GPIO.output(18,GPIO.LOW)
        return "got off"
    else:
        print("user asked for something else")
        return "Hello world!"

# Create a small python server
httpd = make_server("", 8000, simple_app)
print "Serving on port 8000..."
print "You can open this in the browser http://192.168.1.xxx:8000 where xxx is your rpi ip aadress"
print "Or if you run this server on your own computer then http://localhost:8000" 
httpd.serve_forever()
