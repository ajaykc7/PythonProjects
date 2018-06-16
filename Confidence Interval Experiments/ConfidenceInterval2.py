"""
Ajay Kc
013213328
EE381
Project 5 Part 2

The problem calculates the percentage of the sample mean fitting under the area between
various confidence intervals.
"""
import numpy as np
import matplotlib.pyplot as plt
import math as math

bearingList = np.random.normal(75,0.75,1000000)

def checkConfidenceInterval(mean,sd,n,num):
    upper = mean+ num*(sd/math.sqrt(n))
    lower = mean -num*(sd/math.sqrt(n))
    if((75>=lower)and(75<=upper)):
        return "Success"
    else:
        return "Failure"

def estimatePopulationMean(n, confidenceInterval):

    normalList = []
    tDistList = []
    num1=0
    num2={}
    if(confidenceInterval == 95):
        num1 = 1.96

        num2 = {5:2.78,40:2.02,120:1.98}
    else:
        num1 = 2.58
        num2 = {5:4.60,40:2.70,120:2.62}

    for i in range(0, 10000):
        sampleSet = np.random.choice(bearingList,n)
        mean = np.mean(sampleSet)
        sd = np.std(sampleSet)
        normalList.append(checkConfidenceInterval(mean,sd,n,num1))
        tDistList.append(checkConfidenceInterval(mean,sd,n,num2[n]))

    successCountNormal = normalList.count("Success")
    successCounttDist = tDistList.count("Success")
    print("For n = %s" %n)
    print("For %s confidence interval, %s using normal distribution" %(confidenceInterval,successCountNormal/100))
    print("For %s confidence interval, %s using student's t distribution" %(confidenceInterval, successCounttDist / 100))
    print(" ")

estimatePopulationMean(5,95)
estimatePopulationMean(5,99)

estimatePopulationMean(40,95)
estimatePopulationMean(40,99)

estimatePopulationMean(120,95)
estimatePopulationMean(120,99)

