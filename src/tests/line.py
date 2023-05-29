import numpy as np
import cv2

img = cv2.imread(f'../../samples/4.png')

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
vague = cv2.GaussianBlur(grey, (5, 5), 0)

# Apply Canny
contours = cv2.Canny(vague, 50, 150)

# Detect the lines
lines = cv2.HoughLinesP(contours, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

# for line in lines :
#     print(line)
#     cv2.line(img, line[0][0:2], line[0][2:], (255, 0, 0), 3)

line = lines[3]
print(f"Line is {line}")
cv2.line(img, line[0][0:2], line[0][2:], (255, 0, 0), 3)

cv2.imshow('Lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()