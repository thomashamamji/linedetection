import cv2
import os
import json

# For relative filenames
from pathlib import Path
source_path = Path(__file__).resolve()
basefolder = source_path.parent

def main():
    from src.scripts.lines import detect_line

    prePath = "./samples"
    images = os.listdir(prePath)
    images = [cv2.imread(f'{prePath}/{image}') for image in images]

    # Loads the config
    cfgFile = open(f"{basefolder}/config/types.json", 'r')
    typesOpt = json.load(cfgFile)

    for image in images :
        r, line = detect_line(image, typesOpt['filters']['FORWARD'])
        if line is not None :
            print(f"Tracking line : {line}")
            moves = line['moves']
            mx = moves['horizontalMove']
            my1 = moves['firstVerticalDistance']
            my2 = moves['verticalDestination']

if __name__ == "__main__":
    main()