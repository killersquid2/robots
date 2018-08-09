import time
from robot import PinMode, PinValue

PIN_SERVO = 15
PIN_SWITCH = 'a0'

def canHeld(servo_board):
    if servo_board.read_analogue[PIN_SWITCH] > 2.5:
        time.sleep(0.5)
        if servo_board.read_analogue[PIN_SWITCH] > 2.5:
            return True
    return False

def liftCan(servo):
    servo.position = 0

def main(myRobot):
    servo_board = myRobot.servo_board
    servo_board.gpios[PIN_SWITCH].mode = PinMode.INPUT_PULLUP
    servo = servo_board.servos[PIN_SERVO]
	
    servo.position = 1
    
    while not canHeld(servo_board):
        continue
		
    liftCan(servo)
