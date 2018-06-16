"""
Ajay Kc
013213328
EE381
Project 3 Part 1
The program plots a probability mass function of X, where X is the number of "three sixes" received when three dices
are rolled 1000 times
"""
import numpy as np
import matplotlib.pyplot as plt


def rollDices():
    randomVariable = 0  # The variable stores the numerical outcome of getting three sixes
    for i in range(0, 1000):
        diceFaces = np.random.randint(1, 7, 3)
        if (diceFaces.sum() == 18):
            randomVariable += 1

    return randomVariable


def makeFigure(list):
    b = np.arange(0,18)
    h1, bin_edges = np.histogram(list, bins = b)
    b1 = bin_edges[0:17]

    figureOne = plt.figure(1)
    p1 = h1 / 10000
    plt.xticks(b1)
    plt.bar(b1, p1)
    plt.title('Experimental results')
    plt.xlabel('Probability of success')
    plt.ylabel('Frequency')

    plt.show()


randomVariableList = []
for i in range(0, 10000):
    x = rollDices()
    randomVariableList.append(x)

makeFigure(randomVariableList)
