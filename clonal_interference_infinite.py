# @coding: utf-8
# @version: Python 3.8.5
# @date: 2020-11-23
# @author: bastien camillo
# @project: GPOP - Genetic Population

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='This program simulate the evolution of a the allele frequency in a population of 3 alleles')
parser.add_argument('-s1', '--s', type=float, default=1, help='affinity to the allele A')
parser.add_argument('-s2', '--s2', type=float, default=2, help='affinity to the allele B')
parser.add_argument('-s3', '--s3', type=float, default=3, help='affinity to the allele C')
args = parser.parse_args() # parse the arguments

s = args.s
s1 = args.s2
s2 = args.s3


def Z3pop(Z, t, param) : # The function associated with the system
    s, s1, s2 = param
    z = sum(Z)
    res = [
        Z[0]*(s + (((s1)*Z[1]/z) + ((s2)*Z[1]/z))),
        Z[1]*(s1 + (s*Z[0]/z + ((s2)*Z[0]/z))),
        Z[2]*(s2 + (s*Z[0]/z + ((s1)*Z[0]/z)))
    ]
    return res

def main():
    t = np.arange(0.0,10.0,0.001) # Time interval and time step for the integration of the system of ODEs
    y0 = [1.0,1.0,1.0] # Initial values of the system

    param = [s, s1, s2] # Parameters of the system

    y = odeint(Z3pop, y0, t, args=(param,)) # Integration of the system of ODEs
    y = y/np.sum(y, axis=1)[:,None] # Normalization of the solution

    plt.plot(t*100,y[:,0], label = "Allele A", alpha = 0.8)
    plt.plot(t*100,y[:,1], label = "Allele B", alpha = 0.8)
    plt.plot(t*100,y[:,2], label = "Allele C", alpha = 0.8)
    plt.title(f"Evolution of the allele frequencies in a population of 3 alleles\n Allele A: {round(y[-1,0],3)},    Allele B: {round(y[-1,1],3)},    Allele C: {round(y[-1,2],3)}") 
    plt.xlabel("Time")
    plt.ylabel("Allele frequency")
    plt.axis([0,max(t)*100,0,1])
    plt.grid()
    plt.legend()

    plt.savefig(f"clonal_interference_infinite_{s}_{s1}_{s2}.png")
    plt.show()

if __name__ == "__main__":
    main()