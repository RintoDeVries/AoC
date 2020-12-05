
file = open("input_4.txt")
lines = file.readlines()
file.close() 

import re

def check1(passport):
    if len(passport)>=7:
        return True
    else:
        return False

def check2(passport):
    byr = (passport['byr'])
    iyr = (passport['iyr'])
    eyr = (passport['eyr'])  
    hgt = passport['hgt'] 
    ecl = passport['ecl'] 
    pid = passport['pid']
    hcl = passport['hcl']

    if hgt[-2:] not in ['cm', 'in']:
        print ('no cm or inches', hgt)
        return False

    if not byr.isnumeric() or not iyr.isnumeric() or not eyr.isnumeric or not hgt[:-2].isnumeric() or not pid.isnumeric():
        print('weird input', passport)
        return False

    if len(pid)!=9:
        print('wrong passport id', pid)
        return False

    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print('wrong eye colour', ecl)
        return False



    if hgt[-2:]=='cm' and (int(hgt[:-2])<150 or int(hgt[:-2])>193):
        print ('wrong cm length', hgt)
        return False

    if hgt[-2:]=='in' and (int(hgt[:-2])<59 or int(hgt[:-2])>76):
        print ('wrong in length',hgt)
        return False
    

    if int(byr)<1920 or int(byr)>2002:
        print('wrong byr',byr)
        return False

    if int(iyr)<2010 or int(iyr)>2020:
        print('wrong iyr',iyr)
        return False
        
    if int(eyr)<2020 or int(eyr)>2030:
        print('wrong eyr',eyr)
        return False

    if hcl[0]!='#' or bool(re.search(r'^([a-f0-9]){6}$',hcl[1:]))==False:
        print('wrong hcl',hcl)
        return False

    return True 




    
count = 0 
passport  = {} 
for line in lines:
    
    for i in line.split():
        if i[:3]!='cid':
            (key,val)=i.split(':')
            passport[key] = val
            
            
    
    if len(line.strip())==0:
        
        if check1(passport) and check2(passport):
            count+=1
        passport = {} 



