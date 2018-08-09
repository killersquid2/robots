from threading import Thread
from robot import *
from queue import Queue

import canpickup
import motor

#from math import pi
#import time
#import random

r = Robot()
q = Queue()

canpickupThread = Thread(target=canpickup.main, args=(r, q, ))
motorThread = Thread(target=motor.main, args=(r, q, ))

canpickupThread.start()
motorThread.start()

while True:
    continue
