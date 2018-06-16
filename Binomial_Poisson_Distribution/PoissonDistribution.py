"""
Ajay Kc
013213328
EE381
Project 3 Part 3
The program plots a probability mass function of X, where X is the number of "three sixes" received when three dices
are rolled 1000 times. The probability is calculated using the Poisson Distribution
"""
import numpy as np
import matplotlib.pyplot as plt
import math as math

def poissonDistList():
    probabilityOfSuccess = 0.005  # Probability of getting three sixes in one roll of three dice
    n = 1000 #Number of trials
    probabilityList = []
    for randomVariable in range(0, 17):
        probabilityList.append(math.pow(n,randomVariable)*math.pow(probabilityOfSuccess,randomVariable)*
                               math.exp(-n*probabilityOfSuccess)/math.factorial(randomVariable))

    return probabilityList

def makeFigure(list):
    b = np.arange(0,17)
    ##h1, bin_edges = np.histogram(list, bins = b)
    ##b1 = bin_edges[0:17]

    figureOne = plt.figure(1)

    plt.xticks(b)

    plt.bar(b, list)
    plt.title('Experimental results')
    plt.xlabel('Probability of success')
    plt.ylabel('Frequency')

    plt.show()

list = poissonDistList()
makeFigure(list)
