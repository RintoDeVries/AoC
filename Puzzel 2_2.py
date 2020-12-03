file = open("input_2.txt")
lines = file.readlines()
file.close() 

count = 0


def check(pos1,pos2,letter,password):
    if (password[pos1] == letter and password[pos2] !=letter) or (password[pos2] == letter and password[pos1] !=letter):
        return True

    return False 



import re
for line in lines:
    tmp = re.split("-| ",line)
    pos1 = int(tmp[0])-1
    pos2 = int(tmp[1])-1
    letter = tmp[2][0]
    password = tmp[3][:-1]
    if check(pos1,pos2,letter,password):
        count+=1
        

