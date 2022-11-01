import matplotlib.pyplot as plt
import numpy as np
import math
# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html

def fitness_func(solution):
    x = solution[0]
    y = solution[1]
    z=0
    for i in range(0,10):
        for j in range(0,10):
            z+= math.sqrt((i-x)**2  + (j-y)**2)*matriz[i][j]
    return 1/z

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
matriz2 = [[0 for _ in range(10)] for _ in range(10)]
for i in range(0,10):
    for j in range(0,10):
        matriz2[i][j]=fitness_func([i,j])
        
fig,ax = plt.subplots(2)
ax[0].imshow(matriz2, cmap='hot', interpolation='nearest')
ax[1].imshow(matriz, cmap='hot', interpolation='nearest')
plt.show()