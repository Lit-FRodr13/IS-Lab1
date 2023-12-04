import cv2
import numpy as np
from random import random

data = [[0.31565,0.83101,1],
        [0.36484,0.8518,1],
        [0.46111,0.82518,1],
        [0.55223,0.83449,1],
        [0.16975,0.84049,1],
        [0.49187,0.80889,1],
        [0.08838,0.62068,-1],
        [0.098166,0.79092,-1]]

data2 = [[0.21835,0.81884,1],
         [0.14115,0.83535,1],
         [0.37022,0.8111,1],
         [0.14913,0.77104,-1],
         [0.18474,0.6279,-1]]

##P = [x1, x2]

##w1 = np.random.randn(1)
##w2 = np.random.randn(1)
##b = np.random.randn(1)

w1 = random()
w2 = random()
b = random()

total_error = 0.0

for i in range(5):
    
    v = data2[i][0] * w1 + data2[i][1] * w2 + b
    print(str(data2[i][0]) + ', ' + str(data2[i][1]) + ', ' + str(data2[i][2]))
    
    if v > 0:
        y = 1
    else:
        y = -1

    print("output -> " + str(y))

    e = data2[i][2] - y
    print('abs e -> ' + str(abs(e)))
    print()

    total_error = total_error + abs(e)

print('Total error ' + str(total_error))
print('---------------\n')

eta = 0.15 #eta -> learning rate
total_error = 1
counter = 0

while total_error != 0:
    
    for i in range(5):
        
        v = data2[i][0] * w1 + data2[i][1] * w2 + b

        if v > 0:
            y = 1
        else:
            y = -1

        e = data2[i][2] - y
        
        w1 = w1 + eta * e * data2[i][0]
        w2 = w2 + eta * e * data2[i][1]
        b  = b  + eta * e

    total_error = 0
    for i in range(5):
        
        v = data2[i][0] * w1 + data2[i][1] * w2 + b
        #print(str(data2[i][0]) + ', ' + str(data2[i][1]) + ', ' + str(data2[i][2]))

        if v > 0:
            y = 1
        else:
            y = -1

        #print("output -> " + str(y))

        e = data2[i][2] - y
        
        total_error = total_error + abs(e)
        #print('Total error ' + str(total_error) + '\n')

    counter += 1
    
print('Total error training -> ' + str(total_error) + ', iterations: ' + str(counter)+ '\n')

for i in range(8):
    v = data[i][0] * w1 + data[i][1] * w2 + b
    #print(str(data2[i][0]) + ', ' + str(data2[i][1]) + ', ' + str(data2[i][2]))

    if v > 0:
        y = 1
    else:
        y = -1

    #print("output -> " + str(y))

    e = data[i][2] - y

    total_error = total_error + abs(e)
print('Total error testing ' + str(total_error) + '\n')

    
