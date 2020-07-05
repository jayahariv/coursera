import RPi.GPIO as GPIO
from time import sleep

rp_input = 10
rp_output = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(rp_input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(rp_output, GPIO.OUT, initial=GPIO.LOW)

while True: 
    push = GPIO.input(rp_input)
    if(push == GPIO.HIGH):
        GPIO.output(rp_output, GPIO.HIGH)
    else:
        GPIO.output(rp_output, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(rp_output, GPIO.LOW)
        sleep(0.5)
