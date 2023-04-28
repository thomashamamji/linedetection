import json
from json import JSONEncoder
import numpy
import os

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

numpyArrayOne = numpy.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

def countFiles (baseDir) :
    with os.scandir(baseDir) as entries:
        n = 0
        for _ in entries:
            n += 1
    return n

def resolveLineData () :
    baseFolder = os.path.abspath(os.getcwd())
    return f"{baseFolder}/../data/lines"

def get () :
    # Deserialization
    dir = resolveLineData()
    n = countFiles(dir)
    if n == 0 :
        print("Error : no file found for line data storing")
        return ""
    filename = f"{dir}/{n}.json"
    f = open(filename, 'r')
    data = f.read()
    decodedArrays = json.loads(data)
    return numpy.asarray(decodedArrays["lines"])

def add (entry) :
    # Serialization
    numpyData = {"lines": entry}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)
    dir = resolveLineData()
    n = countFiles(dir)
    filename = f"{dir}/{n+1}.json"
    f = open(filename, "w")
    f.write(encodedNumpyData)
    f.close()