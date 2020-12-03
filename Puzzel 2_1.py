file = open("input_2.txt")
lines = file.readlines()
file.close() 

count = 0

import re
for line in lines:
    tmp = re.split("-| ",line)
    minimum = int(tmp[0])
    maximum = int(tmp[1])
    letter = tmp[2][0]
    password = tmp[3][:-1]
    if (password.count(letter)<=maximum) and (password.count(letter)>=minimum):
        count+=1
        
