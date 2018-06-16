"""
Ajay Kc
013213328
EE381
Project 4 Part 2

The problem simulates the exponentially distributed RV and plots the histogram for the simulated
results. Finally, it plots the plot for exponentially distributed RV
"""

import numpy as np
import math
import matplotlib.pyplot as plt
def simulateRV():

    RV = np.random.exponential(0.5,10000)
    return RV

def plotFunctions(RV):
    nbins=30; # Number of bins
    edgecolor = 'w';    #Color seperating bars in the bargraph
    #
    #Create bins and histogram
    bins = [float(x) for x in np.linspace(1, 4, nbins+1)]
    h1, bin_edges = np.histogram(RV, bins, density = True)
    #Define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0] #Width of bars in the bargraph

    figureOne = plt.figure(1)
    xlabel = "Random Variable (T)"
    plt.xlabel(xlabel, fontsize = 20)
    plt.ylabel("f(T) = 2exp(-2T)", fontsize = 20)
    plt.title("Exponentially Distributed R.V function and histogram",fontsize=20)
    plt.bar(b1,h1,width = barwidth, edgecolor=edgecolor)

    exponentialDist = []
    for i in range(0, len(b1)):
        exponentialDist.append(2*math.exp(-2*b1[i]))
    plt.plot(b1, exponentialDist, color='r')

    plt.show()

RV = simulateRV()
plotFunctions(RV)
