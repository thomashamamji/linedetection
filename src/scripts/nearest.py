import numpy as np
import lib.serial as ser
import os
import cv2
import sys

logPath = "../../log/nearest.log"

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

def findNearest (lines) :
    bottomCorners = []
    topCorners = []
    lineDistances = []

    distancesList = []
    rectangleSizeList = []
    rectangles = []

    for l in lines :
        newLine = []
        for i, _ in enumerate(l[0]) :
            newLine.append([_])
        bl, tl, tr, br = newLine

        newTopCorner = [ tl, tr ]
        newBottomCorner = [ bl, br ]

        internal.log(f"Adding new top corner : {newTopCorner}")
        internal.log(f"Adding new bottom corner : {newBottomCorner}")

        topCorners.append(newTopCorner)
        bottomCorners.append(newBottomCorner)

        # Calculating the distance
        newDistance = tr[0][0][Y] - br[0][0][Y]
        internal.log(f"Adding new distance {newDistance}")
        lineDistances.append(newDistance) # The minimum between the two top and bottom corners can be taken as the value to take to calculate the distance

        internal.log(f"4 points : {newLine}")
        internal.log(f"Bottom line : {bl}, {br}")

        # Filtering
        distances = [np.absolute(newLine[0][0][0]-newLine[idx][0][0]) for idx in range(1, 4)] # Calculating the distances
        distances = np.array(distances)

        recSize = distances.sum()
        rectangleSizeList.append(recSize) # Sum of the distances of the matrix

        recLength = newDistance
        bl = np.array(bl)
        bl = bl.tolist()
        br = np.array(br)
        br = br.tolist()
        bottomLineHeight = [bl[0][0], br[0][0]]

        rec = {
            'distances' : distances.tolist(), # All distances
            'size' : recSize, # Perimeter of the rectangle
            'length' : recLength,
            'position' : np.array(newLine),
            'bottom' : bottomLineHeight # Position of the two bottom corners of the rectangle
        }

        distancesList.append(distances)
        rectangles.append(rec)

    distancesList = np.array(distancesList)
    internal.log(f"Distances matrix : {distancesList}")
    internal.log(f"Rectangle size list : {rectangleSizeList}")

    bottomCorners = np.array(bottomCorners)
    
    # Sorting
    rectangles.sort(key=lambda x: x['size'], reverse=True)
    rectangles.sort(key=lambda x: x['bottom'][0][Y], reverse=False)
 
    bottomLines = [rec['bottom'] for rec in rectangles]
    nearestLine = None
 
    # Getting the first element of the sorted list
    if len(rectangles) > 0 :
        nearestLine = rectangles[0]
    
    # Logging the results
    internal.log(f"Bottom lines : {bottomLines}")
    internal.log(f"Nearest line : {nearestLine['bottom']}")
    internal.log(f"Distances : {lineDistances}")
    internal.log(f"Rectangles : {rectangles}")
    internal.log(f"Distances list : {distancesList}")

    return (nearestLine, mIndex(lines, nearestLine.get('line')))

def drawLineContours (img, line) :
    internal.log(f"Drawing line {line} ...")
    cv2.drawContours(img, [line], 0, (0, 255, 0), 5)

def drawNearest (img, contours) :
    nl, nContour = findNearest(linesList)
    internal.log(f"nContour : {nContour}")
    drawLineContours(img, nl['line'])

# Function calls

images = os.listdir("../../samples")

for image in images :
    img = cv2.imread(f'../../samples/{image}')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    linesList = ser.get()
    internal.log(f"Lines {linesList}")

    # Finding nearest line's element and index
    nl, idx = findNearest(linesList)
    internal.log(f"Nearest line : {nl}")
    internal.log(f"Index : {idx}")