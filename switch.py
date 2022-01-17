import RPi.GPIO as GPIO

#Pin setup
GPIO.setmode(GPIO.BOARD)

#Setting pin 0 to be an input and have an initial "off" value
GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#function checks the state of the switch
def get_switch():
    if GPIO.input(0) == GPIO.HIGH:
        return 1
    else:
        return 0
