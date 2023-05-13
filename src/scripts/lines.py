import cv2
import numpy as np
import sys
from lib import test
import nearest
import os

logPath = "../../logs/lines.log"

sys.path.insert(1, logPath)
from lib.logger import LOG
internal = LOG(logPath)

def diminuer_luminosite(image, gamma):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

def detect_line(img):
    # Get the size
    h, w, c = img.shape

    # Convert the image
    lum = diminuer_luminosite(img, 0.45)
    grey = cv2.cvtColor(lum, cv2.COLOR_BGR2GRAY)
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

    nls = nearest.findNearest((h,w), lines)
    internal.log(f"Lines with distances : {nls}")

    if len(nls) > 6 :
        for _ in range(3) :
            nl = nls[_]
            nlps = nl['position']
            cv2.line(img, nlps[0:2], nlps[2:], (0, 0, 255), 3)

    # Store the result
    test.writeResult(img, 0)

# Function calls

images = os.listdir("../../samples")
images = [cv2.imread(f'../../samples/{image}') for image in images]
for image in images :
    detect_line(image)