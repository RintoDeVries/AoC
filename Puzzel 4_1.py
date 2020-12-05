import numpy as np 


file = open("input_4.txt")
lines = file.readlines()
file.close() 


def check(set1, set2):
    if len(set1&set2)>=7:
        return True

    else:
        return False 






set1 = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} 





count = 0 

set2 = set() 
for line in lines:
    set2 = set2.union(set([i[:3] for i in line.split()]))
    
        
    if len(line.strip())==0:
        #print(set2)
        if check(set1, set2):
            count+=1 
        set2 = set() 



