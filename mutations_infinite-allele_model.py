# @coding: utf-8
# @version: Python 3.8.4
# @date: 2020-11-23
# @author: bastien camillo
# @project: GPOP - Genetic Population

import random
import matplotlib.pyplot as plt
import argparse
from alive_progress import alive_bar
import pandas as pd
from math import sqrt

parser = argparse.ArgumentParser(description="This script simulate the evolution of a population with mutations")
parser.add_argument('-sim', '--sim', type=int, default=10, help='Number of simulations')
parser.add_argument('-size', '--size', type=int, default=100, help='Size of the population')
parser.add_argument('-mut', '--mutation_rate', type=float, default=0.01, help='Mutation rate')
parser.add_argument('-gen', '--gen', type=int, default=1000, help='Number of generations')
args = parser.parse_args() # parse the arguments

simu = args.sim
size = args.size
mutation_rate = args.mutation_rate
gen = args.gen

class population():
    '''
    This class is used to create a population of individuals
    '''
    def __init__(self, size : int, µ : float):
        '''
        This function initialize the parameters of the population from generation 0
        ----------------
        parameters
        size: int -> the size of the population
        µ: float -> mutation rate
        '''
        self.size = size #size of the population
        self.generation = 0 #number of the generation
        self.population = [] #list of the individuals of the population
        self.fitness = {} #fitness of the population
        self.fitness_list = [] #list of the fitness of the population
        self.mutation_rate = µ #mutation rate
        self.population = [int(0) for i in range(self.size)] #create the population

    def get_fitness(self) -> float: #get the fitness of the population
        dic = {}
        for k in self.population:
            if f"{k}" not in dic :
                dic[f"{k}"] = self.population.count(k)/self.size
        return dic

    #create new generation from the last one
    def next_generation(self):
        '''
        This function create the next generation from the last one
        '''
        #create a new generation        
        #self.population = [random.choice(self.population) if random.random() < self.mutation_rate else int(max(self.population())+1) for i in range(self.size)]
        
        for i in range(self.size):
            if random.random() < self.mutation_rate:
                self.population[i] = max(self.population)+1                
            else:
                self.population[i] = random.choice(self.population)
        
        self.fitness = self.get_fitness() #get the fitness of the population
        self.fitness_list.append(self.fitness) #add the fitness to the fitness list
        self.generation += 1 #add 1 to the generation number

    def get_generation(self) -> int: #get the generation number
        return self.generation
    
    def get_fitness_list(self) -> list: #get the fitness list
        return self.fitness_list

    def get_population(self) -> list: #get the population list
        return self.population

def main():
    plt.figure(figsize=(16,9))
    plt.suptitle("Fitness of the population")
    for sim in range(simu):
        pop = population(size, mutation_rate) #create the population
        for j in range(gen):
            pop.next_generation()  

        #get the fitness list
        fitness_list = pop.get_fitness_list()    

        df = pd.DataFrame(fitness_list)
        df = df.fillna(0)

        plt.subplot(int(sqrt(simu)), int(sqrt(simu))+1, sim+1)
        plt.plot(df)
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.title(f"Simulation {sim+1}")

    plt.tight_layout()
    plt.savefig(f"Mutations_{simu}_{size}_{mutation_rate}_{gen}.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()
