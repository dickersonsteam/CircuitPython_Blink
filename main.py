# main.py
# CircuitPython Blink

import time
from digitalio import DigitalInOut, Direction
import board

# define constants
delayTime = 0.5

led = DigitalInOut(board.D6)
led.direction = Direction.OUTPUT

while True:
    led.value = False
    time.sleep(delayTime) # delay half second
    led.value = True
    time.sleep(delayTime)
