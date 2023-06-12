import json
from os import getcwd


# For relative filenames
from pathlib import Path
source_path = Path(__file__).resolve()
basefolder = source_path.parent

# Loads the config
cfgFile = open(f"{basefolder}/../../config/distances.json", 'r')
typesOpt = json.load(cfgFile)


with open(f"{basefolder}/../../config/types.json", 'r') as optFile :
    distances = json.loads(optFile.read())

X = 0
Y = 1


"""

0.45 < x < 0.5 => d : 65
0.5 < x < 0.55 => d : 60

"""

# Based on the value in pixels of 20 cm

def convert(pixels, widget) :
    size, axis = widget
    if axis == X :
        rate = (size // 2 + pixels) / size
        print(f"Rate is {rate}")
        for dist in distances['X'] :
            if dist['rate'] is not None :
                rates = list(dist['rate'])
                # Required
                if len(rates) == 2 :
                    if rates[0] != -1 and rates[1] == -1 and rate >= rates[0] :
                        return (20 // dist['distance']) * pixels
                    elif rates[0] == -1 and rates[1] != -1 and rate <= rates[0] :
                        return (20 // dist['distance']) * pixels
                    elif rates[0] != -1 :
                        print("Correct rates !")
                        if rates[0] <= rate and rates[1] >= rate :
                            return int((20 / dist['distance']) * pixels)
                    
    if axis == Y :
        if pixels <= 80 :
            return pixels * 2
        elif pixels >= 110 and pixels <= 130 :
            return pixels - 30
    return 0

def test (pixels, size) :
    finalDistance = convert(pixels, (size, X))
    print(f"Distance for {pixels} pixels is {finalDistance}")