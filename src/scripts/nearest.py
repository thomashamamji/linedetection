import numpy as np
import json

# For relative filenames
from pathlib import Path
source_path = Path(__file__).resolve()
basefolder = source_path.parent

# Loads the config
cfgFile = open(f"{basefolder}/../../config/types.json", 'r')
typesOpt = json.load(cfgFile)

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
        for i, _ in enumerate(l[0]) :
            newLine.append([_])
        newLine = [nl[0] for nl in newLine]
        x1, y1, x2, y2 = newLine

        # Distance to the center
        dx = -1
        cx = w // 2

        if x1 >= cx :
            dx = x1-cx
        else :
            dx = cx-x1
        
        distanceX = np.absolute(dx)

        # Length calculus
        ly = np.maximum(y1,y2) - np.minimum(y1,y2)
        lx = np.maximum(x1, x2) - np.minimum(x1, x2)
        l = lx
        onY = ly >= lx
        if onY :
            l = ly

        # Adding the values
        newLines.append({
            'id' : idx,
            'position' : newLine,
            'distanceX' : distanceX,
            'distanceY' : np.maximum(y1,y2),
            'length' : l,
            'onY' : onY
        })
    
    filters = typesOpt['filters']
    # Sorting
    if cr == filters['LENGTH'] :
        newLines.sort(key=lambda x : x['length'], reverse=True) # The nearest from the bottom
    if cr == filters['FORWARD'] :
        newLines.sort(key=lambda x : x['distanceX'], reverse=False) # The nearest from the center
    if cr == filters['BOTTOM'] :
        newLines.sort(key=lambda x : x['distanceY'], reverse=False) # The nearest from the bottom (fails)

    return newLines