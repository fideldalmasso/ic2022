from numpy.random import rand, randint
import numpy as np
import matplotlib.pyplot as plt
 
def objective_function(I):
    x = I[0]
    y = I[1]
    Objective_min = 0.26*(x**2 + y**2) - 0.48*x*y
    Objective_max = 1/(1 + Objective_min) # Convert the min to max problem
     
    return Objective_max
 
# Parameters of the binary genetic algorithm
bounds = [[-10, 10], [-10, 10]]
iteration = 200
bits = 20 # number of bits for each variable
pop_size = 100
crossover_rate = 0.8
mutation_rate = 0.2

# Initial population
pop = [randint(0, 2, bits*len(bounds)).tolist() for _ in range(pop_size)]
print("xd")