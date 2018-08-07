def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def main(myRobot):
	m = myRobot.motor_board
	
	lastRight = 0.95
	lastLeft = 1
		
	while True:
		leftDrive = 1
		rightDrive = 0.95
		
		front = r.servo_board.read_ultrasound(6, 7)
		left = r.servo_board.read_ultrasound(10, 11)
		right = r.servo_board.read_ultrasound(8, 9)
		
		# if were approaching a wall we should start to turn
		if front < 0.7 and right < 0.5:
			leftDrive = translate(front, 0, 0.7, 1, 0)
		elif right > 0.8:
			rightDrive = 0.75
		else:
			leftDrive = 1
			

		lastRight = (rightDrive + lastRight)/2
		lastLeft = (leftDrive + lastLeft)/2
		m.m1 = lastRight
		m.m0 = lastLeft
		