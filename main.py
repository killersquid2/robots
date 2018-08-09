from threading import Thread
from robot import *

import canpickup
import motor

#from math import pi
#import time
#import random

r = Robot()

canpickupThread = Thread(target=canpickup.main, args=(r,))
motorThread = Thread(target=motor.main, args=(r,))

canpickupThread.start()
motorThread.start()

while True:
    continue
