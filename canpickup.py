import time
from robot import PinMode

PIN_SERVO = 0
PIN_SWITCH = 1

def canHeld():
	if servo_board.gpios[PIN_SWITCH].read() == PinValue.LOW:
		time.sleep(2)
	    if servo_board.gpios[PIN_SWITCH].read() == PinValue.LOW:
			return True
	return False

def liftCan(servo):
	servo.position = 1

def main(myRobot):
	motor_board = myRobot.motor_board
	servo_board = myRobot.servo_board
	power_board = myRobot.power_board
	
	servo_board.gpios[PIN_SWITCH].mode = PinMode.INPUT_PULLUP
	
	servo = servo_board.servos[PIN_SERVO]
	servo.position = 0
	
	while not canHeld():
		continue
	liftCan(servo)
