import numpy as np
from itertools import combinations


data = np.genfromtxt("input.txt", dtype='uintc')
for item in combinations(data,3):
    if sum(item)==2020:
        print(item[0]*item[1]*item[2])
