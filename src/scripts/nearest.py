import numpy as np
import sys
import json
import math

# For relative filenames
from pathlib import Path
source_path = Path(__file__).resolve()
basefolder = source_path.parent

# Loads the config
cfgFile = open(f"{basefolder}/../../config/types.json", 'r')
typesOpt = json.load(cfgFile)

logPath = f"{basefolder}/../../logs/nearest.log"

sys.path.insert(1, logPath)
from .lib.logger import LOG
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

# Finds the nearest line based on a criteria
def findNearest (dim, lines, cr) :
    h, w = dim
    newLines = []

    for idx, l in enumerate(lines) :
        newLine = []
        # This loop must disappear
        for i, _ in enumerate(l[0]) :
            newLine.append([_])
        newLine = [nl[0] for nl in newLine]
        x1, y1, x2, y2 = newLine

        internal.log(f"4 points : {newLine}")

        # Distance to the center
        dx = -1
        cx = w // 2

        dir = 1
        if x1 >= cx :
            dx = x1-cx
            dir = -1
        else :
            dx = cx-x1

        if dx < 0 :
            internal.log(f"Got a negative dx : {dx}")
        
        horizontalDistance = np.absolute(dx)

        # Length calculus
        ymax = np.maximum(y1, y2)
        xmax = np.maximum(x1, x2)
        ymin = np.minimum(y1, y2)
        xmin = np.minimum(x1, x2)

        ly = ymax - ymin
        lx = xmax - xmin

        # Points to reach
        yStart = h-ymax
        yEnd = h-ymax+l
        dy = yEnd-yStart

        # The angle calculus
        cos = xmax / ymax
        # theta = math.acos(cos)

        # Maybe not necessary
        l = lx
        onY = ly >= lx
        if onY :
            l = ly

        verticalDistance = h-ymax

        # Adding the values
        newLines.append({
            'id' : idx,
            'xDist' : horizontalDistance,
            'length' : l,
            'position' : newLine,
            'moves' : {
                'firstVerticalDistance' : verticalDistance,
                'verticalDestination' : verticalDistance+l,
                'horizontalMove' : dir * horizontalDistance
            }
        })
    
    filters = typesOpt['filters']
    # Sorting
    if cr == filters['LENGTH'] :
        newLines.sort(key=lambda x : x['length'], reverse=True) # The nearest from the bottom
    if cr == filters['FORWARD'] :
        newLines.sort(key=lambda x : x['xDist'], reverse=False) # The nearest from the center
    if cr == filters['BOTTOM'] :
        newLines.sort(key=lambda x : x['distanceY'], reverse=False) # The nearest from the bottom (fails)
    
    # Logging the results
    internal.log(f"New lines (W:{w},H:{h}) : {newLines}")

    return newLines