import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 50)
pwm.start(0)

duty = 1;
dir = True; # true = increasing; false = decreasing
while True: 
    pwm.ChangeDutyCycle(duty)
    
    if (duty == 100) or (duty == 0):
        dir = not dir 
    
    duty = duty + 1 if dir else duty - 1
    sleep(0.01)

