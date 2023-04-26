import cv2
import numpy as np
from matplotlib import pyplot as plt
from lib import test

img = cv2.imread('../samples/routes.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Setting threshold of gray image
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0

# Setting operations for any type of line detection
HORIZONTAL = 0
VERTICAL = 1

DIST = 10
DIRECTION = VERTICAL

lineChunks = []
positions = []

for contour in contours:
	if i == 0:
		i = 1
		continue

	approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

    # Positions
	x = -1
	y = -1

	M = cv2.moments(contour)
	if M['m00'] != 0.0:
		x = int(M['m10']/M['m00'])
		y = int(M['m01']/M['m00'])

	# Detecting lines as rectangles
	if len(approx) == 4:
		positions.append([x,y])
		# Keeping the largest line chunks
		newApprox = approx[np.absolute(approx[0][0][DIRECTION]-approx[1][0][DIRECTION]) > DIST] # Depends on the chosen direction
		if (len(newApprox)>0) :
			lineChunks.append(newApprox)
			# Drawing the contour (red)
			cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)

test.writeResult(img, 1)

# Displaying the positions

n = len(positions)

if n > 20 :
	n = n // 10

print(f"Positions : {positions[:n]}")
print(f"Line chunks ({len(lineChunks)}) : {lineChunks}")