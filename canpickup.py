import time
from robot import PinMode, PinValue

PIN_SERVO = 15
PIN_SWITCH = 2

def canHeld(servo_board):
    if servo_board.gpios[PIN_SWITCH].read() == PinValue.LOW:
        time.sleep(2)
        if servo_board.gpios[PIN_SWITCH].read() == PinValue.LOW:
            return True
    return False

def liftCan(servo):
    servo.position = 1

def main(myRobot):
    servo_board = myRobot.servo_board
    servo_board.gpios[PIN_SWITCH].mode = PinMode.INPUT_PULLUP
    servo = servo_board.servos[PIN_SERVO]
	
    servo.position = 0
    
    while not canHeld(servo_board):
        continue
		
    liftCan(servo)
