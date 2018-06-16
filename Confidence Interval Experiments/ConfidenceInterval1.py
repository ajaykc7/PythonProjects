"""
Ajay Kc
013213328
EE381
Project 5 Part 1

The problem plots two plots showing the effect of confidence intervals on sample size.
"""
import numpy as np
import matplotlib.pyplot as plt
import math as math
mean = 75
sd = 0.75

#method to generate 1000000 numbers with mean 75 and standard deviation as 0.75
def generateNumbers():

    Nlist = np.random.normal(75,0.75,1000000)
    return Nlist

#method to generate a sample of size n from the list
def generateSample(list,n):

    sample = []
    sample = np.random.choice(list,n)

    return sample

def plotGraph(meanList,confidenceInterval):

    plt.xlabel('Sample size',fontsize=20)
    plt.ylabel('X bar',fontsize=20)
    plt.title('Sample Means and '+str(confidenceInterval)+"% confidence Intervals",fontsize=20)

    #plot a straight line through the mean
    plt.axhline(y=75, color='black')

    #plot the sample
    plt.scatter(range(1,201),meanList,marker='x')

    #plot the confidence interval
    e=0
    if(confidenceInterval==95):
        e = 1.96
    else:
        e = 2.58
    confidenceIntervalList1 = []
    confidenceIntervalList2 = []
    for i in range(1,201):
        confidenceIntervalList1.append(mean+e*(sd/math.sqrt(i)))
        confidenceIntervalList2.append(mean - e * (sd / math.sqrt(i)))

    plt.plot(range(1,201),confidenceIntervalList1,'--',color='red')
    plt.plot(range(1, 201), confidenceIntervalList2, '--', color='red')

    plt.show()

bearingList = generateNumbers()
meanList = []
standardDeviationList = []
for i in range(1,201):

    sampleList = generateSample(bearingList,i)

    meanList.append(np.mean(sampleList))
    standardDeviationList.append(np.std(sampleList))

plotGraph(meanList,95)
plotGraph(meanList,99)
