import numpy as np
import lib.serial as ser
import cv2

lines = ser.get()
print(f"Lines {lines}")

bottomCorners = []
nearestLine = lines[0].min(0)

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

    rec = {
        'distances' : distances.tolist(),
        'size' : recSize,
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

print(f"Bottom corners : {bottomCorners}")

nearestLine = bottomCorners.min(1)

print(f"Rectangles : {rectangles}")