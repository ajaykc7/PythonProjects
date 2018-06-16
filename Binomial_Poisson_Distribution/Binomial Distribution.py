import numpy as np
import matplotlib.pyplot as plt
import math as math

def nCr(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

def binomialDistList():
    probabilityOfSuccess = 0.005 #Probability of getting three sixes in one roll of three dice
    probabilityList =[]
    for randomVariable in range(0, 17):
        probabilityList.append(nCr(1000,randomVariable)*(math.pow(probabilityOfSuccess,randomVariable))*
                               (math.pow(1-probabilityOfSuccess,1000-randomVariable)))

    return probabilityList

def makeFigure(list):
    b = np.arange(0,17)

    figureOne = plt.figure(1)

    plt.xticks(b)

    plt.bar(b, list)
    plt.title('Experimental results')
    plt.xlabel('Probability of success')
    plt.ylabel('Frequency')

    plt.show()

list = binomialDistList()
makeFigure(list)
