These programs have been coded for the final project of GPOP 2022 by Bastien CAMILLO.
The code is available on GitHub.

The code is written in Python 3.8.4 and uses the following libraries:
    - numpy, pandas, matplotlib, alive_progress, scipy
    - random, math, argparse

GPOP: simulating an evolving population

    The objective of the project is the simulation of a simple population-genetics model to observe the influence of
    genetic drift, mutations, selection and population structure on the evolution of the population. The simulations will
    be done using a clonal version of the Wright-Fisher model.

    1) Genetic drift
    -- genetic_drif.py --
    This program simulates the evolution of a population under the effect of genetic drift.
    The program takes 3 arguments:
    - size: the size of the population
    - gen: the number of generations
    - sim: the number of simulations
    A figure is generated at the end of the simulation.

    2) Coalescent model
    -- coalescent_model.py --
    This program simulates the evolution of a population and retrieve the last coalescent event time and last common ancestor.
    The program takes 3 arguments:
    - size: the size of the population
    - sim: the number of simulations
    - max_iter: the maximum number of iterations

    3) Mutations in the infinite-allele model
    -- mutations_infinite-allele_model.py --
    This program simulates the evolution of a population under the effect of mutations.
    The program takes 4 arguments:
    - size: the size of the population
    - gen: the number of generations
    - sim: the number of simulations
    - mut: the mutation rate

    4) Selection
    -- selection_infinite.py --
    This program simulates the evolution of alleles frequency under the effect of selection with two alleles.
    The program takes 1 argument:
    - s: the selection coefficient
    A figure is generated at the end of the simulation.

    5) Clonal interference
    -- clonal_interference_infinite.py --
    This program simulates the evolution of alleles frequency with three alleles.
    The program takes 3 arguments:
    - s1: the selection coefficient for allele A
    - s2: the selection coefficient for allele B
    - s3: the selection coefficient for allele C
    A figure is generated at the end of the simulation.

    6) Population structure
    -- population_structure.py --
    This program simulate the evolution of a population subdivided in 10 subpopulations under the effect of genetic drift without migration.
    The program takes 3 arguments:
    - s: the size of the population
    - p: the probability to inherit the allele A
    - g: the number of generations
    A figure is generated at the end of the simulation.

    7) Migration
    -- migration.py --
    This program simulate the evolution of a population subdivided in 10 subpopulations under the effect of genetic drift with migration.
    The program takes 4 arguments:
    - s: the size of the population
    - p: the probability to inherit the allele A
    - g: the number of generations
    - m: the migration rate
    A figure is generated at the end of the simulation.