import cv2 as cv
import os
import json

# These are the path from scripts/ folder
def writeResult(content, t) :
    with open('../config/types.json', "r") as f :
        types = json.load(f)
        dir = types['values'][t]
        baseDir = f"../results/{dir}"

        with os.scandir(baseDir) as entries:
            n = 1
            for _ in entries:
                n += 1
            cv.imwrite(f'{baseDir}/{n}.jpg', content)