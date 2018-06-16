"""
Ajay Kc
013213328
EE381
Project 4 Part 1

The problem plots a probability distribution function of S, where S is a Random Variable of sum 
of the widths of n books. The value of n is 1,5,10,and 15. For each value of n, the experimental 
PDF and normal distribution function is calculated.
"""
import numpy as np
import math
import matplotlib.pyplot as plt
mean = (1+3)/2
standard_deviation = math.sqrt(((3-1)**2)/12)

def getRVMean(n):
    return n*mean

def getRVSd(n):
    return standard_deviation*math.sqrt(n)

def simulateRV(n):

    RV = []
    for i in range(0,10000):
        thickness = np.random.uniform(1,3,n)
        RV.append(thickness.sum())
    return RV

def plotFunctions(RV,n):
    a = 1; b =3 #a = min width; b = max width
    nbooks =n; nbins=30; #Number of books; Number of bins
    edgecolor = 'w';    #Color seperating bars in the bargraph
    #
    #Create bins and histogram
    bins = [float(x) for x in np.linspace(nbooks*a, nbooks*b, nbins+1)]
    h1, bin_edges = np.histogram(RV, bins, density = True)
    #Define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0] #Width of bars in the bargraph

    figureOne = plt.figure(1)
    xlabel = "Book stack height for n="+str(n)+" books"
    plt.xlabel(xlabel, fontsize = 20)
    plt.ylabel("PDF", fontsize = 20)
    plt.title("PDF of book stack height and comparison with Gaussian",fontsize=20)
    plt.bar(b1,h1,width = barwidth, edgecolor=edgecolor)

    normalDist = []
    for i in range(0,len(b1)):
        normalDist.append((1 / (getRVSd(n) * math.sqrt(2 * math.pi))) * math.exp(
            -((b1[i] - getRVMean(n)) ** 2) / (2 * getRVSd(n) ** 2)))

    plt.plot(b1,normalDist,color='r')
    plt.show()

#For 1 book
RV = simulateRV(1)
plotFunctions(RV,1)

#For 5 books
RV = simulateRV(5)
plotFunctions(RV,5)

#For 10 books
RV = simulateRV(10)
plotFunctions(RV,10)

#For 15 books
RV = simulateRV(15)
plotFunctions(RV,15)
