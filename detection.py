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
        detect_line(image, typesOpt['filters']['FORWARD'])

if __name__ == "__main__":
    main()