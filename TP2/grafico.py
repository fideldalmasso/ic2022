import pygad
import numpy
import math
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def fitness2(num):
    fitness=0
    xfs = int(num/10)%10
    yfs = num%10
    for i in range(0,10):
        for j in range(0,10):

            fitness+= math.sqrt((i-xfs)**2  + (j-yfs)**2)*matriz[i][j]
        
    return -fitness

matriz = [
    [5,2,4,8,9,0,3,3,8,7],
    [5,5,3,4,4,6,4,1,9,1],
    [4,1,2,1,3,8,7,8,9,1],
    [1,7,1,6,9,3,1,9,6,9],
    [4,7,4,9,9,8,6,5,4,2],
    [7,5,8,2,5,2,3,9,8,2],
    [1,4,0,6,8,4,0,1,2,1],
    [1,5,2,1,2,8,3,3,6,2],
    [4,5,9,6,3,9,7,6,5,10],
    [0,6,2,8,7,1,2,1,5,3]
]

valoresx = range(0,100)
y = [fitness2(x) for x in valoresx]
print(y.index(max(y)))
print(max(y))
plt.plot(valoresx, y, color="red")
plt.show()