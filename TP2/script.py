import pygad
import numpy
import math


# https://blog.paperspace.com/working-with-different-genetic-algorithm-representations-python/
# https://pygad.readthedocs.io/en/latest/

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


"""
Given the following function:
    y = f(w1:w6) = w1x1 + w2x2 + w3x3 + w4x4 + w5x5 + 6wx6
    where (x1,x2,x3,x4,x5,x6)=(4,-2,3.5,5,-11,-4.7) and y=44
What are the best values for the 6 weights (w1 to w6)? We are going to use the genetic algorithm to optimize this function.
"""

function_inputs = [1,1,1,1,1,1,1,1] # Function inputs.
desired_output = 44 # Function output.


def binatodeci(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))

def fitness2(num):
    xfs = int(num/10)%10
    yfs = num%10
    for i in range(0,10):
        for j in range(0,10):

            fitness+= math.sqrt((i-xfs)**2  + (j-yfs)**2)*matriz[i][j]
        
    return -fitness

def fitness_func(solution, solution_idx):
    # output = numpy.sum(solution*function_inputs)
    # fitness = 1.0 / (numpy.abs(output - desired_output) + 0.000001)
    # return fitness
    fitness = 0
    num = binatodeci(solution)
    xfs = ((num/16)/16)*10  #256 -> 12 % 10 -> 2
    yfs = ((num%16)/16)*10
    for i in range(0,10):
        for j in range(0,10):

            fitness+= math.sqrt((i-xfs)**2  + (j-yfs)**2)*matriz[i][j]
        
    return -fitness

num_generations = 50    # Number of generations.
num_parents_mating = 4  # Number of solutions to be selected as parents in the mating pool.
sol_per_pop = 6        # Number of solutions in the population.
num_genes = len(function_inputs)

last_fitness = 0
def on_generation(ga_instance):
    global last_fitness
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]))
    print("Change     = {change}".format(change=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1] - last_fitness))
    print("x Best Solution: " +str(binatodeci(ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[0])))
    last_fitness = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       fitness_func=fitness_func,
                       on_generation=on_generation,
                       parent_selection_type="rws",
                       mutation_by_replacement=True,
                       keep_elitism=2,
                       init_range_low=0,
                       init_range_high=2,
                       gene_type=int,
                       allow_duplicate_genes= False                    
)
# Running the GA to optimize the parameters of the function.
ga_instance.run()

ga_instance.plot_fitness()

# Returning the details of the best solution.
solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)
print("Parameters of the best solution : {solution}".format(solution=solution))
print("x Best Solution: " +str(binatodeci(solution)))
num = binatodeci(solution)
xfs = ((num/16)/16)*10  #256 -> 12 % 10 -> 2
yfs = ((num%16)/16)*10
print("x Best Solution: " +str(xfs)+" y Best Solution: "+str(yfs))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

prediction = numpy.sum(numpy.array(function_inputs)*solution)
print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

if ga_instance.best_solution_generation != -1:
    print("Best fitness value reached after {best_solution_generation} generations.".format(best_solution_generation=ga_instance.best_solution_generation))

# Saving the GA instance.
filename = 'genetic' # The filename to which the instance is saved. The name is without extension.
ga_instance.save(filename=filename)

# Loading the saved GA instance.
loaded_ga_instance = pygad.load(filename=filename)
loaded_ga_instance.plot_fitness()