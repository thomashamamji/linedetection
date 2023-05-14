import cv2
import numpy as np
import sys
from . import nearest
from .lib import test, logger
import json

# For relative filenames
from pathlib import Path
source_path = Path(__file__).resolve()
basefolder = source_path.parent

# Loads the config
cfgFile = open(f"{basefolder}/../../config/types.json", 'r')
typesOpt = json.load(cfgFile)

logPath = f"{basefolder}/../../logs/lines.log"

sys.path.insert(1, logPath)
internal = logger.LOG(logPath)

def diminuer_luminosite(image, gamma):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

def detect_line(img, filterType):
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
        for line in lines:
            x1, y1, x2, y2 = line[0]
            internal.log(f"[{x1},{x2},{y1},{y2}]")
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

        nls = nearest.findNearest((h,w), lines, filterType)
        nNls = len(nls)
        nls2 = list(nls)
        nls2.sort(key=lambda x : x['id'],reverse=False)
        internal.log(f"New lines detected ({nNls}) : {nls2}")

        if len(nls) > 1 :
            for _ in range(1) :
                nl = nls[_]
                nlps = nl['position']
                internal.log(f"Red drawing line {nl['id']} ...")
                cv2.line(img, nlps[0:2], nlps[2:], (0, 0, 255), 3)

        # Store the result
        test.writeResult(img, 0)