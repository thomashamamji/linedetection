import numpy as np
import lib.serial as ser
import os
import cv2

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

    distancesList = []
    rectangleSizeList = []
    rectangles = []

    for l in lines :
        newLine = []
        for i, _ in enumerate(l[0]) :
            newLine.append([_])
        bl, tl, tr, br = newLine
        bottomCorners.append([ bl, br ])

        print(f"4 points : {newLine}")
        print(f"Bottom line : {bl}, {br}")

        # Filtering
        distances = [np.absolute(newLine[0][0][0]-newLine[idx][0][0]) for idx in range(1, 4)] # Calculating the distances
        distances = np.array(distances)

        recSize = distances.sum()
        rectangleSizeList.append(recSize) # Sum of the distances of the matrix

        bl = np.array(bl)
        bl = bl.tolist()
        bottomLineHeight = bl[0][0]
        recLength = -1 # Needs to be calculated

        rec = {
            'distances' : distances.tolist(),
            'size' : recSize,
            'length' : recLength,
            'line' : np.array(newLine),
            'bottom' : {
                'height' : bottomLineHeight
            }
        }

        distancesList.append(distances)
        rectangles.append(rec)

    distancesList = np.array(distancesList)
    print(f"Distances matrix : {distancesList}")

    print(f"Rectangle size list : {rectangleSizeList}")

    bottomCorners = np.array(bottomCorners)
    
    # Sorting
    rectangles.sort(key=lambda x: x['size'], reverse=True)
    rectangles.sort(key=lambda x: x['bottom']['height'][Y], reverse=False)
 
    rectangleBottoms = [rec['bottom'] for rec in rectangles]
    print(f"Rectangles : {rectangleBottoms}")
    nearestLine = None
 
    # Getting the first element of the sorted list
    if len(rectangles) > 0 :
        nearestLine = rectangles[0]
    print(f"Nearest line : {nearestLine['bottom']}")

    return (nearestLine, mIndex(lines, nearestLine['line']))

def drawLineContours (img, line) :
    print(f"Drawing line {line} ...")
    cv2.drawContours(img, [line], 0, (0, 255, 0), 5)

def drawNearest (img, contours) :
    nl, nContour = findNearest(linesList)
    print(f"nContour : {nContour}")
    drawLineContours(img, nl['line'])

# Function calls

images = os.listdir("../samples")

for image in images :
    img = cv2.imread(f'../samples/{image}')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    linesList = ser.get()
    print(f"Lines {linesList}")

    # Finding nearest line's element and index
    nl, idx = findNearest(linesList)
    print(f"Nearest line : {nl}\nIndex : {idx}")