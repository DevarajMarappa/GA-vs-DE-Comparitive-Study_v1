import numpy as np
import matplotlib.pyplot as plt
import random
import benchmarkFunctions
import struct

dims = [2,10,20]
number_of_runs = 31
pop_size=100
mf=0.8 #mutation factor
Cr=0.9 #crossover rate
problem_dimension=None

# Mutation
def mutation(population, target_index):
    a, b, c = random.sample(range(pop_size), 3)
    mutant = population[a] + mf * (population[b] - population[c])
    return mutant

# DE Crossover
def deCrossover(population, target_index, mutant, prblm_dim):
    target = population[target_index]
    trial = np.copy(target)
    for i in range(prblm_dim):
        if random.random() < Cr:
            trial[i] = mutant[i]
    return trial

# Initialize  population
def init_population(population_size, problem_dimension):
    population = []
    for _ in range(population_size):
        individual = np.random.uniform(-10, 10, problem_dimension)
        population.append(individual)
    return population

# Main algorithm loop
def de_logic(problem_dimension,benfunc):           
    population = init_population(pop_size, problem_dimension)
    best_solution = None
    best_fitness = float('-inf')
    fitness_values = []  # Store fitness values for plotting
    for generation in range(number_of_runs):
        nfc = 0  # Number of fitness evaluations
        max_nfc=3000*problem_dimension
        while nfc < max_nfc:  
            for i in range(pop_size):
                target = population[i]
                mutant = mutation(population, i)
                trial = deCrossover(population, i, mutant, problem_dimension)
                target_fitness , func_name = benchmarkFunctions.evaluate_functions(benfunc,target)
                trial_fitness, func_name = benchmarkFunctions.evaluate_functions(benfunc,trial)
                if trial_fitness > target_fitness:
                    population[i] = trial
                    if trial_fitness > best_fitness:
                        best_solution = trial
                        best_fitness = trial_fitness
                if nfc >= max_nfc:
                    break
            fitness_values.append(best_fitness) 
    fitness_values.sort(reverse=True)
    mean=str( np.mean(best_solution))
    std=str( np.std(best_solution))
    variance=str( np.var(best_solution))
    print("----------------------------- FUNC NAME  ------------- :"+func_name +"  --------DIMENSION------------"+ str(problem_dimension))
    print("mean is : "+mean)
    print("std is : "+std)
    print("var is : "+variance)   
    generations = range(1, number_of_runs+1 )
    
    out =struct
    out.func_name=func_name
    out.best_solution=best_solution
    out.fitness_values=fitness_values
    out.best_fitness=best_fitness
    out.problem_dimension=problem_dimension
    out.generations=generations
    out.mean=mean
    out.mean=std
    out.mean=variance
    return out
