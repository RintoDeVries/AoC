import numpy as np 


file = open("input_5.txt")
lines = file.readlines()
file.close() 




def calc_seatid(bp):
    rowmin,rowmax = 0,127
    colmin,colmax = 0,7
    
    for i in bp:
        if i == 'B':
            rowmin = rowmin + 0.5*(rowmax-rowmin+1)
        if i == 'F':
            rowmax =  rowmax - 0.5*(rowmax-rowmin+1)
        if i == 'L':
            colmax =  colmax - 0.5*(colmax-colmin+1)
        if i == 'R':
            colmin = colmin + 0.5*(colmax-colmin+1)
    return int(colmax+rowmax*8)


def missing_elements(L):
    start, end = L[0], L[-1]
    return sorted(set(range(start, end + 1)).difference(L))

maximum =0
seatids = []

for line in lines:
    seatid = calc_seatid(line)
    seatids.append(seatid)
    if seatid>maximum:
        maximum = seatid

seatids.sort()
print(missing_elements(seatids))
print(maximum)

