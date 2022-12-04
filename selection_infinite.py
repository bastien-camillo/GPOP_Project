# @coding: utf-8
# @version: Python 3.8.5
# @date: 2020-11-23
# @author: bastien camillo
# @project: GPOP - Genetic Population

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--s', dest='s', type=float, required=True, help='affinity to the allele B')
args = parser.parse_args() # parse the arguments

s = args.s

def Z2pop(Z, t, s) : # The function associated with the system
    z = sum(Z)
    res = [
        Z[0]*(1 + ((1+s)*Z[1]/z)),
        Z[1]*((1+s) + (Z[0]/z))
    ]
    return res

def main():
    t = np.arange(0.0,10.0,0.001) # Time interval and time step for the integration of the system of ODEs
    y0 = [1.0,1.0] # Initial values of the system

    y = odeint(Z2pop, y0, t, args=(s,)) # Integration of the system of ODEs
    y = y/np.sum(y, axis=1)[:,None] # Normalization of the solution

    plt.plot(t*100,y[:,0], label = "Allele A", alpha = 0.8)
    plt.plot(t*100,y[:,1], label = "Allele B", alpha = 0.8)
    plt.title(f"Evolution of the allele frequencies in a population of 3 alleles\n Allele A: {round(y[-1,0],3)},    Allele B: {round(y[-1,1],3)}") 
    plt.xlabel("Time")
    plt.ylabel("Allele frequency")
    plt.axis([0,max(t)*100,0,1])
    plt.grid()
    plt.legend()

    plt.savefig(f"clonal_interference_infinite_{s}.png")
    plt.show()

if __name__ == "__main__":
    main()