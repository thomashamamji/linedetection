import cv2
import numpy as np
import sys
from lib import test
import os

logPath = "../../logs/lines.log"

sys.path.insert(1, logPath)
from lib.logger import LOG
internal = LOG(logPath)

def detect_line(img):
    # Convert the image
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    vague = cv2.GaussianBlur(grey, (5, 5), 0)

    # Apply Canny
    contours = cv2.Canny(vague, 50, 150)

    # Detect the lines
    lines = cv2.HoughLinesP(contours, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

    # Draw the lines
    if lines is not None:
        internal.log(f"New lines detected !")
        for line in lines:
            x1, y1, x2, y2 = line[0]
            internal.log(f"[({x1},{x2},{y1},{y2})]")
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

    # Store the result
    test.writeResult(img, 0)

# Function calls

images = os.listdir("../../samples")
images = [cv2.imread(f'../../samples/{image}') for image in images]
for image in images :
    detect_line(image)