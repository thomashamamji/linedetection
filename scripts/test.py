import numpy as np
import lib.serial as ser

def mIndex (l, element) :
    idx = -1
    for index, row in enumerate(l) :
        if element in row :
            idx = index
    return idx

lines = ser.get()
print(lines)
idx1 = np.where(lines == lines[0])
idx2 = np.where(lines == lines[1])
idx3 = np.where(lines == lines[2])

idx1 = mIndex(lines, lines[1])
idx2 = mIndex(lines, lines[1])
idx3 = mIndex(lines, lines[2])

print(f"idx 1 = {idx1}\nidx 2 = {idx2}\nidx 3 = {idx3}")