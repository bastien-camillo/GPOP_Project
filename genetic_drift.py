# @coding: utf-8
# @version: Python 3.8.4
# @date: 2020-11-23
# @author: bastien camillo
# @project: GPOP - Genetic Population

import random
import matplotlib.pyplot as plt
import argparse
from alive_progress import alive_bar

parser = argparse.ArgumentParser(description='Genetic drift simulation')
parser.add_argument('-sim', '--sim', type=int, default=100, help='Number of simulations')
parser.add_argument('-size', '--size', type=int, default=100, help='Size of the population')
parser.add_argument('-gen', '--gen', type=int, default=1000, help='Number of generations')
args = parser.parse_args() # parse the arguments

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
        self.fitness = 0 #fitness of the population
        self.fitness_list = [] #list of the fitness of the population
        self.population = [] #list of the individuals of the population
        self.population = [self.get_individual() for i in range(self.size)] #create the population
        self.fitness = self.get_fitness() #get the fitness of the population
        self.fitness_list.append(self.fitness) #add the fitness to the fitness list

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

    def get_genotypes(self) -> list: #get the genotypes of the population in a list
        return [i.genotype for i in self.population] 
    
    def get_fitness(self) -> float: #get the fitness of the population
        return self.get_genotypes().count('A') / self.size
    
    #create new generation from the last one
    def next_generation(self):
        '''
        This function create the next generation from the last one
        '''
        self.population = [random.choice(self.population) for i in range(self.size)] #create the new population
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
    '''
    Here we create a population of 100 individuals with a probability of p in range(0.1, 1, 0.1) to have the allele A.
    We do 100 simulations for each probability p and we plot the fitness of the population for each probability p for 1000 generations.
    '''
    plt.figure( figsize=(15, 8) )
    plt.suptitle('Evolution of the fitness of a population with genetic drift')

    size = args.size #size of the population
    generations = args.gen #number of generations
    nb_simulations = args.sim #number of simulations

    with alive_bar( int(9*nb_simulations*generations), ctrl_c=True, title=f"Simulation\t") as bar:
        for j in range(1,10): #for each probability p in range(0.1, 1, 0.1)
            plt.subplot(3,3, j) #create a subplot

            p = j/10 #probability of having the allele A
            cpt_A = 0 #number of individuals with the allele A in the population at the end of the simulation 

            # We do nb_simulations simulations for each probability p
            for k in range(nb_simulations):
                #create the population
                pop = population(size, p) 
                bar()
                #create the next generation
                for i in range(generations):
                    pop.next_generation()
                    bar()

                #get the genotypes of the population
                if pop.get_genotypes().count('A') > pop.get_genotypes().count('B'): 
                    cpt_A += 1
                
                #plot the fitness of the population for each probability p for 1000 generations
                plt.plot(pop.get_fitness_list())

            plt.title("Fitness over generations\np_expected = " + str(p) + ", p_observed = " + str(cpt_A/nb_simulations))
            plt.xlabel("Generations")
            plt.ylabel("Fitness")

    plt.tight_layout() #adjust the layout
    plt.savefig(f'genetic_drift_{args.sim}_{args.size}_{args.gen}.png',dpi= 300) #save the figure
    plt.show()    

if __name__ == '__main__':
    main()
