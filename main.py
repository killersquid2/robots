from threading import threading
from robot import *

import canpickup
import motor

#from math import pi
#import time
#import random

r = Robot()

canpickupThread = threading.Thread(target=canpickup, args=(r))
motorThread = threading.Thread(target=motor, args=(r))

canpickupThread.start()
motorThread.start()

print('done')