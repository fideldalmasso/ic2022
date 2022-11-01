import pygad
import math
import matplotlib.pyplot as plt
import numpy as np

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

def fitness_func(solution, solution_idx):
    x = solution[0]
    y = solution[1]
    # Z = -(100*(x**2 - y)**2 + (1 - x)**2)
    z=0
    for i in range(0,10):
        for j in range(0,10):
            z+= math.sqrt((i-x)**2  + (j-y)**2)*matriz[i][j]
        
    return 1/z
    # return Z

last_fitness = 0
def on_generation(ga_instance):
    global last_fitness
    print("-> Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]))
    print("Change     = {change}".format(change=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1] - last_fitness))
    print("Best Solution: " +str(ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[0]))
    print("Population: ",end=" ")
    for x in ga_instance.population:
        print(f'[{int(x[0])},{int(x[1])}]',end=" ")
    print("")
    last_fitness = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]

ga_instance = pygad.GA(num_generations=20,
                       num_parents_mating=2,
                       sol_per_pop=4,
                       num_genes=2,
                    #    gene_space={"low": 0, "high": 10},
                       gene_space=[0,1,2,3,4,5,6,7,8,9],
                       mutation_by_replacement=True,
                       fitness_func=fitness_func,
                       on_generation=on_generation,
                       save_solutions=True)

ga_instance.run()


solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)
print("Solution", solution)
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

ga_instance.plot_fitness()
ga_instance.plot_genes()