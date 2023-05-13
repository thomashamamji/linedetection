import numpy as np
import lib.serial as ser
import os
import cv2
import sys

logPath = "../../logs/nearest.log"

sys.path.insert(1, logPath)
from lib.logger import LOG
internal = LOG(logPath)
internal.log("Starting the nearest line script ...")

X = 0
Y = 1

def mIndex (l, element) :
    idx = -1
    for index, row in enumerate(l) :
        if element in row :
            idx = index
    return idx

def findNearest (dim, lines) :
    h, w = dim
    bottomCorners = []
    newLines = []

    for idx, l in enumerate(lines) :
        newLine = []
        for i, _ in enumerate(l[0]) :
            newLine.append([_])
        newLine = [nl[0] for nl in newLine]
        x1, y1, x2, y2 = newLine

        internal.log(f"4 points : {newLine}")

        bottomLine = [(x1,y1), (x2,y2)]
        bottomCorners.append(bottomLine) # positions of : [ left, right ]

        # Distance to the center
        # Problem here
        dx = x2 - (w//2)
        dy = y2 - (h//2)
        distanceX = np.absolute(dx)
        distanceY = np.absolute(dy)
        
        newLines.append({
            'id' : idx,
            'position' : newLine,
            'distanceX' : distanceX,
            'distanceY' : distanceY
        })
    
    # Sorting
    newLines.sort(key=lambda x : x['distanceY'], reverse=False) # The nearest from the bottom
    # newLines.sort(key=lambda x : x['distanceX'], reverse=True) # The nearest from the center

    nearestLine = None
 
    # Getting the first element of the sorted list
    if len(newLines) > 0 :
        nearestLine = newLines[0]
    
    # Logging the results
    internal.log(f"New lines ({h, w}) : {newLines}")

    return newLines