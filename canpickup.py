import time
from robot import PinMode, PinValue

PIN_SERVO = 15
PIN_SWITCH = 'a0'

def canHeld(servo_board, myQueue):
    if servo_board.read_analogue()[PIN_SWITCH] > 2.5:
        myQueue.put("STOP")
        time.sleep(0.2)
        if servo_board.read_analogue()[PIN_SWITCH] > 2.5:
            return True
    return False

def liftCan(servo):
    servo.position = 0

def main(myRobot, myQueue):
    servo_board = myRobot.servo_board
    servo = servo_board.servos[PIN_SERVO]
    
    servo.position = 1
    
    while not canHeld(servo_board, myQueue):
        continue
    	
    liftCan(servo)
    time.sleep(0.2)
    myQueue.put("START")
    
