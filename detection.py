import cv2
import os
import json

X = 0
Y = 1

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
        r, line, moves = detect_line(image, typesOpt['filters']['FORWARD'])

        if line is not None :
            print(f"Tracking line : {line}")
            x1, y1, y2 = moves
            print(f"Moves are :\n1 - {x1}\n2 - {y1}\n1 - {y2}\n")

if __name__ == "__main__":
    main()