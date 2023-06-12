import json
from os import getcwd


# For relative filenames
from pathlib import Path
source_path = Path(__file__).resolve()
basefolder = source_path.parent

# Loads the config
cfgFile = open(f"{basefolder}/../../../config/distances.json", 'r')
distances = json.load(cfgFile)


with open(f"{basefolder}/../../../config/types.json", 'r') as optFile :
    typesOpt = json.loads(optFile.read())

X = 0
Y = 1


"""

0.45 < x < 0.5 => d : 65
0.5 < x < 0.55 => d : 60

"""

# Based on the value in pixels of 20 cm

def checkDist (dist) :
    if dist < 10 :
        return 0
    elif dist < 20 :
        return 20
    else :
        return dist
    
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
                        val = int((20 / dist['distance']) * pixels)
                        return checkDist(val)
                    
                    elif rates[0] == -1 and rates[1] != -1 and rate <= rates[0] :
                        val = int((20 / dist['distance']) * pixels)
                        print(f"Val is {val}")
                        return checkDist(val)
                    
                    elif rates[0] != -1 :
                        if rates[0] <= rate and rates[1] >= rate :
                            val = int((20 / dist['distance']) * pixels)
                            return checkDist(val)
                    
    if axis == Y :
        if pixels <= 80 :
            val = int((20 / (pixels * 2)) * pixels)
            return checkDist(val)

        elif pixels >= 110 and pixels <= 130 :
            val = int((20 / (pixels - 30)) * pixels)
            return checkDist(val)
        # Must be spliten into multiple distances
        else :
            return 30
    return 0

def test (pixels, widget) :
    finalDistance = convert(pixels, widget)
    print(f"Distance for {pixels} pixels is {finalDistance} cm")