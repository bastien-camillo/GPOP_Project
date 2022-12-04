# @coding: utf-8
# @version: Python 3.8.5
# @date: 2020-11-23
# @author: bastien camillo
# @project: GPOP - Genetic Population

import random
import matplotlib.pyplot as plt
import argparse
from alive_progress import alive_bar

parser = argparse.ArgumentParser(description='This program simulate the evolution of a population subdivided in 10 subpopulations without migration')
parser.add_argument('-s', '--size', type=int, default=1000, help='size of the non subdivided population')
parser.add_argument('-p', '--p', type=float, default=0.5, help='probability of having the allele A')
parser.add_argument('-g', '--generations', type=int, default=1000, help='number of generations')
args = parser.parse_args()

size = args.size
p = args.p
generations = args.generations

class population():
    '''
    This class is used to create a population of individuals
    '''
    def __init__(self, size : int, p : float):
        '''
        This function initialize the parameters of the population from generation 0
        ----------------
        parameters
        size: int -> the size of the population
        p: float -> the probability of having the genotype A
        '''
        self.size = size #size of the population
        self.p = p #probability of having the allele A
        self.generation = 0 #number of the generation
        self.fitness = [] #fitness of the population
        self.fitness_list = {f"{int(i)}":[] for i in range(10)} #list of the fitness of the population
        self.population = [self.get_individual() for i in range(self.size)] #create the population
        self.subpopulations = [self.population[i:i+int(self.size/10)] for i in range(0, self.size, int(self.size/10))]
        self.fitness = self.get_fitness() #get the fitness of the population
        self.get_fitness_list() #add the fitness to the fitness list

    class individual():
        '''
        This class is used to create individuals. Each individual has a probability p to have the allele A
        '''
        def __init__(self, p : float):
            '''
            This function initialize the parameters of the individual
            ------------------------------------
            parameter
            self: the individual
            p: float -> probability of having the allele A
            ------------------------------------
            output
            self.genotype: the genotype of the individual
            '''
            self.p = p #probability of having the allele A
            self.genotype = 'A' if random.random() < self.p else 'B' #create the genotype of the individual with the probability p

        def get_genotype(self): #get the genotype of the individual
            return self.genotype

    def get_individual(self) -> individual: #get an individual
        return self.individual(self.p)

    def get_genotypes_of(self, pos : int) -> list: #get the genotypes of the population in a list
        return [i.genotype for i in self.subpopulations[pos]]
    
    def get_genotypes(self) -> list: #get the genotypes of the population in a list
        return [self.get_genotypes_of(i) for i in range(len(self.subpopulations))] 
    
    def get_fitness(self) -> float: #get the fitness of the population
        return [self.get_genotypes_of(i).count('A') / self.size for i in range(len(self.subpopulations))] 
    
    def get_fitness_list(self) -> list:
        for i in range(len(self.subpopulations)):
            self.fitness_list[f"{int(i)}"].append(self.fitness[i])
    
    #create new generation from the last one
    def next_generation(self):
        '''
        This function create the next generation from the last one
        '''
        self.subpopulations = [[random.choice(self.subpopulations[j]) for i in range(self.size)] for j in range(len(self.subpopulations))] #create the new subpopulations without migration
        self.population = [item for sublist in self.subpopulations for item in sublist] #create the new population        
        self.fitness = self.get_fitness() #get the fitness of the population
        self.get_fitness_list() #add the fitness to the fitness list
        self.generation += 1 #add 1 to the generation number

    def out_generation(self) -> int: #get the generation number
        return self.generation
    
    def out_fitness_list(self) -> list: #get the fitness list
        return self.fitness_list

    def out_population(self) -> list: #get the population list
        return self.population

    def out_subpopulations(self) -> list: #get the subpopulations list
        return self.subpopulations

def main():
    pop = population(size, p) #create the population
    with alive_bar(generations) as bar:
        for i in range(generations): #loop over the generations
            pop.next_generation() #create the next generation
            bar()

    plt.figure(figsize=(16, 9))
    for i in range(10):
        plt.plot(range(generations+1)[1:], pop.fitness_list[f"{int(i)}"][1:], label=f'subpopulation {i+1}')
    plt.title('Population structure')
    plt.xlabel('Generation')
    plt.ylabel('Frequency of allele A')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig(f"population_structure_-m_{size}_{p}_{generations}.png")
    plt.show()

if __name__ == '__main__':
    main()