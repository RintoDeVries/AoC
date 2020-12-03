import numpy as np 


file = open("input_3.txt")
lines = file.readlines()
file.close() 


slope = 1
matrix = np.zeros((323,2480))



for row,line in enumerate(lines):

    tmp = 80* [int(i) for i in line[:-1]]
    matrix[row] = tmp
        


running = True
row = 0
col =0
maxrow = len(matrix)-1
count =0
totalcount =1 


while running:
    count+=matrix[row,col]
    row+=2
    col+=1

    if row>maxrow:
        break 






