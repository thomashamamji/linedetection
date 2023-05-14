import cv2 as cv
import os
import json

# For relative filenames
from pathlib import Path
source_path = Path(__file__).resolve()
basefolder = source_path.parent

# These are the path from scripts/ folder
def writeResult(content, t) :
    with open(f'{basefolder}/../../../config/types.json', "r") as f :
        types = json.load(f)
        dir = types['values'][t]
        baseDir = f"{basefolder}/../../../results/{dir}"

        with os.scandir(baseDir) as entries:
            n = 1
            for _ in entries:
                n += 1
            cv.imwrite(f'{baseDir}/{n}.jpg', content)