# main.py
# CircuitPython Blink

import time
from digitalio import DigitalInOut, Direction
import board

led = DigitalInOut(board.D6)
led.direction = Direction.OUTPUT

while True:
    led.value = False
    time.sleep(0.5) # delay half second
    led.value = True
    time.sleep(0.5)
