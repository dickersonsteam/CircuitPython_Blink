# main.py
# blink built-in and user-added LED

import board
import time
from digitalio import DigitalInOut, Direction

# create IO objects
# be sure to replace D13 and D2
# with pins appropriate to your board
led = DigitalInOut(board.D13)  # built-in LED
myLed = DigitalInOut(board.D2)  # led added by user in circuit

# initialize pins as outputs
led.direction = Direction.OUTPUT
myLed.direction = Direction.OUTPUT

# initialize LED states
led.value = True
myLed.value = True

while True:
    led.value = not led.value
    myLed.value = not myLed.value
    
    time.sleep(1)
    
