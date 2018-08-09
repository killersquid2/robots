PIN_ULTRA_R_ECHO = 2
PIN_ULTRA_R_TRIG = 3
PIN_ULTRA_L_ECHO = 4
PIN_ULTRA_L_TRIG = 5
PIN_ULTRA_F_ECHO = 6
PIN_ULTRA_F_TRIG = 7

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def main(myRobot, myQueue):
    motor_board = myRobot.motor_board
    servo_board = myRobot.servo_board

    lastLeft = 0
    lastRight = 0

    run = True
    
    while True:
        if not myQueue.empty():
            print("item in queue")
            item = myQueue.get()
            if item == "STOP":
                run = False
            elif item == "START":
                run = True
        if run:
            leftDrive = 1
            rightDrive = 0.95

            front = servo_board.read_ultrasound(PIN_ULTRA_F_TRIG, PIN_ULTRA_F_ECHO)
            left = servo_board.read_ultrasound(PIN_ULTRA_L_TRIG, PIN_ULTRA_L_ECHO)
            right = servo_board.read_ultrasound(PIN_ULTRA_R_TRIG, PIN_ULTRA_R_ECHO)

            # if were approaching a wall we should start to turn
            if front < 0.7 and right < 0.5:
                leftDrive = translate(front, 0, 0.7, 1, 0)
            elif right > 0.8:
                rightDrive = 0.75
            else:
                leftDrive = 1

            lastRight = (rightDrive + lastRight)/2
            lastLeft = (leftDrive + lastLeft)/2

            motor_board.m0 = lastLeft
            motor_board.m1 = lastRight
        else:
            motor_board.m0 = 0
            motor_board.m1 = 0
            
##
