# @coding: utf-8
# @version: Python 3.8.5
# @date: 2020-11-23
# @author: bastien camillo
# @project: GPOP - Genetic Population

import random
import argparse

parser = argparse.ArgumentParser(description='Simulate population genetics and retrieve the coalescent event time and last common ancestor')
parser.add_argument('-size', '--size', type=int, default=100, help='Size of the population')
parser.add_argument('-sim', '--sim', type=int, default=10, help='Number of simulations')
parser.add_argument('-max_iter', '--max_iter', default=1000, type=int, help='Maximum number of iterations')
args = parser.parse_args() # parse the arguments

size = args.size
simu = args.sim
max_iter = args.max_iter

class population():
    '''
    This class is used to create a population of individuals
    '''
    def __init__(self, size : int):
        '''
        This function initialize the parameters of the population from generation 0
        ----------------
        parameters
        size: int -> the size of the population
        ----------------
        output
        self.size: int -> the size of the population
        self.generation: int -> the number of the generation
        self.population: list -> the list of the individuals of the population
        '''
        self.size = size #size of the population
        self.generation = 0 #number of the generation
        self.population = [] #list of the individuals of the population
        self.population = [self.get_individual() for i in range(self.size)] #create the population

    class individual():
        '''
        This class is used to create individuals.
        '''
        def __init__(self):
            '''
            This function initialize the parameters of the individual
            ------------------------------------
            parameter
            self: the individual
            ------------------------------------
            output
            self.ancestors: list of the ancestors of the individual
            '''            
            self.ancestors = [] #list of the ancestors of the individual

    def get_individual(self) -> individual: #get an individual
        return self.individual()
   
    #create new generation from the last one
    def next_generation(self):
        '''
        This function create the next generation from the last one
        '''
        ids = [random.randint(0,self.size-1) for i in range(self.size)] #create the new population
        old_pop = self.population.copy() #copy the old population

        self.population = [] #create the new population
        for i in ids: # for each individual in the new population
            self.population.append(self.individual()) #create the new population
            self.population[-1].ancestors = old_pop[i].ancestors + [i] #add the ancestors of the individual
        
        self.generation += 1 #add 1 to the generation number

    def get_generation(self) -> int: #get the generation number
        return self.generation
    
    def get_population(self) -> list: #get the population list
        return self.population

    def get_ancestors(self) -> list: #get the ancestors list
        return [i.ancestors for i in self.population]

def last_coalescent_event(group : list) -> dict:
    '''
    Find the common ancestor of a group of individuals if it exists
    -----------------
    parameter
    group: list of individuals -> the group of individuals
    -----------------
    output
    individual: dict -> the common ancestor of the group if it exists, None otherwise 
    '''
    for i in reversed(range(len(group[0].ancestors))): #for each generation in the ancestors of the first individual of the group in reverse order
        #if all the individuals of the group have the same ancestor at the generation i 
        if all([(group[j].ancestors)[i] == group[0].ancestors[i] for j in range(len(group))]):            
            return {'ancestor' : group[0].ancestors[i], 'generation' : len(group[0].ancestors) - i}
    return {'ancestor' : None, 'generation' : None}

def all_identical_by_descent(pop : population) -> bool:
    '''
    Check if all the individuals of the population are identical by descent
    -----------------
    parameter
    pop: population -> the population
    -----------------
    output
    bool: bool -> True if all the individuals are identical by descent, False otherwise
    '''
    for k in range(len(pop.get_population()[0].ancestors)):
        # si tous les individus ont le même ancêtre à la génération k alors ils sont identiques par descendance
        if all([pop.get_population()[j].ancestors[k] == pop.get_population()[0].ancestors[k] for j in range(len(pop.get_population()))]):
            return True

def get_subpopulation(pop : population, group : list) -> list:
    '''
    Get the subpopulation of a group of individuals
    -----------------
    parameters
    pop: population -> the population
    group: list -> the group of individuals
    -----------------
    output
    subpopulation: list -> the subpopulation of the group
    '''
    subpopulation = []
    for i in group:
        subpopulation.append(pop.get_population()[i])
    return subpopulation

def get_subpopulation_ancestors(pop : population, group : list) -> list:
    '''
    Get the ancestors of the subpopulation of a group of individuals
    -----------------
    parameters
    pop: population -> the population
    group: list -> the group of individuals
    -----------------
    output
    ancestors: list -> the ancestors of the subpopulation of the group
    '''
    return [i.ancestors for i in get_subpopulation(pop, group)]


def get_subpopulation_ancestors_last_coalescent_event(pop : population, group : list) -> int:
    '''
    Get the last coalescent event of the ancestors of the subpopulation of a group of individuals
    -----------------
    parameters
    pop: population -> the population
    group: list -> the group of individuals
    -----------------
    output
    event: int -> the last coalescent event of the ancestors of the subpopulation of the group
    '''
    return last_coalescent_event(get_subpopulation(pop, group))


def main():
    '''
    This function is used to run the simulations
    '''
    pop = population(size) #create the population
    
    pop.next_generation()
    
    cpt = 0
    while not all_identical_by_descent(pop) and cpt < max_iter:
        pop.next_generation()
        cpt += 1
    
    if cpt == max_iter:
        print("The maximum number of iterations has been reached")
    else:
        descent = last_coalescent_event(pop.get_population())
        print(f"They are all identical by decent at the generation {descent['generation']} with the ancestor {descent['ancestor']}")

        simulations = 10
        for sim in range(simulations):
            group = [random.randint(0, pop.size-1) for i in range(random.randint(2,5))]
            result = get_subpopulation_ancestors_last_coalescent_event(pop, group)
            print(f"The last coalescent event of the group {group} is at the generation {result['generation']} with the ancestor {result['ancestor']}")

if __name__ == "__main__":
    main()