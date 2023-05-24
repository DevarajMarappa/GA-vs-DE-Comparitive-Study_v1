from ypstruct import structure
import matplotlib.pyplot as plt
import numpy as np
import time

import gaCrossOver
import deAlgo

pop_size = 100 #np
crossover_rate = 0.9 #cr
dimensions=[2,10,20]

#DE
# Run the DE for each benchmark fucntions
for i in range(1,9):
  process_start =None
  process_end=None
  outDE=None
  outGA=None
  # Run the DE for each problem dimension
  for dim in dimensions:
    process_start=time.perf_counter()
    outDE=deAlgo.de_logic(dim,i) #de plot are part of the DE logic implementation
    process_end=time.perf_counter()
    process_start=time.perf_counter()
    outGA=gaCrossOver.ga_logic(dim,i)
    x=np.multiply( np.arange(31),100*dim)
    process_end=time.perf_counter()
    print("DE Tot Time for Dimension : "+str(dim)+" is : "+str(process_end-process_start))

    plt.plot(x, outDE.fitness_values, label="DE",linestyle="-.")
    plt.plot(x, outGA.gafitness_values, label="GA",linestyle=":")
    plt.xlabel('NFCs')
    plt.ylabel('Best fitness error sp far')
    plt.title('Optimization Progress : '+outDE.func_name + ' , Dimension : '+str(outDE.problem_dimension))
    plt.grid(True)
    plt.legend()
    plt.savefig("plots//"+outDE.func_name+"_"+str(outDE.problem_dimension)+"_plot.png")
    #plt.show()
    plt.clf()
    print(f"**DE** Best Solution:  {outDE.best_solution}, Best Fitness: {outDE.best_fitness}")
    print(f"**GA** Best Solution:  {outGA.gabest_solution}, Best Fitness: {outGA.GAbest_fitness}")

  

    
     


