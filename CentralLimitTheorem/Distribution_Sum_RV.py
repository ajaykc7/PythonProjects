"""
Ajay Kc
013213328
EE381
Project 4 Part 3

The problem simulates the lifespan of a carton with 24 batteries and plots the histogram
for the simulated results.
"""
import numpy as np
import matplotlib.pyplot as plt
import math as math
mean = 45
standard_deviation = 45

def getRVMean(n):
    return n*mean

def getRVSd(n):
    return standard_deviation*math.sqrt(n)

def simulateExpRV():
    expRV = np.random.exponential(45,100)
    return expRV

def simulateSumExpEV():
    carton = []
    sumRV = []

    for i in range (0,24):
        carton.append(simulateExpRV())

    sumRV = [sum(x) for x in zip(*carton)]

    return sumRV

def plotFunctions(RV):
    nbins=30; # Number of bins
    nbatteries = 24
    a=20
    b=70
    edgecolor = 'w';    #Color seperating bars in the bargraph
    #
    #Create bins and histogram
    bins = [float(x) for x in np.linspace(nbatteries*a, nbatteries*b, nbins+1)]
    h1, bin_edges = np.histogram(RV, bins, density = True)
    #Define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0] #Width of bars in the bargraph

    figureOne = plt.figure(1)
    xlabel = "Life span of 24 batteries"
    plt.xlabel(xlabel, fontsize = 20)
    plt.ylabel("PDF", fontsize = 20)
    plt.title("PDF of life span of 24 batteries and comparison with Gaussian",fontsize=20)
    plt.bar(b1,h1,width = barwidth, edgecolor=edgecolor, color = 'b')

    normalDist = []
    for i in range(0, len(b1)):
        normalDist.append((1 / (getRVSd(24) * math.sqrt(2 * math.pi))) * math.exp(
            -((b1[i] - getRVMean(24)) ** 2) / (2 * getRVSd(24) ** 2)))

    plt.plot(b1, normalDist, color='r')
    plt.show()
    plt.close()

    H1 = np.cumsum(h1)*barwidth
    xlabel = "Life span of 24 batteries"
    plt.xlabel(xlabel, fontsize=20)
    plt.ylabel("CDF", fontsize=20)
    plt.title("CDF of life span of 24 batteries", fontsize=20)

    plt.bar(b1,H1,width = barwidth, edgecolor=edgecolor)
    plt.show()
    plt.close()

mergedList = []
for i in range(0,10000):
    mergedList += simulateSumExpEV()

plotFunctions(mergedList)
