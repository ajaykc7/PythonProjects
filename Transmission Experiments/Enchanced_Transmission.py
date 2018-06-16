"""
Ajay Kc
013213328
EE 381
Project 1 Part 4

The program calculates the probability of a transmitted signal being received incorrectly
when a 0 or 1 is transmitted and the same bit is trasmitted three times
"""

import numpy as np
p = 0.4 #Probability that generated bit is 0
e0 = 0.02 #Probability of transmission error when transmitted signal is 1
e1 = 0.03 #Probability of transmission error when transmitted signal is 0

def transmitSignal():

    m = np.random.rand()
    if ( m <=p):
        return 0
    else:
        return 1

def receiveSignal(bitTransmitted):

    bits=""
    for i in range (0,3):
        m = np.random.rand()
        if(bitTransmitted==0):
            if(m<=e0):
              bit = 1
            else:
              bit = 0
        else:
            if(m<=e1):
                bit = 0
            else:
                bit = 1

        bits = bits + str(bit)

    return bits

count=0
for i in range(0,100000):
    bitTransmitted = transmitSignal()
    bitsReceived = receiveSignal(bitTransmitted)
    if(bitsReceived.count("0")>bitsReceived.count("1")):
        bit = 0
    else:
        bit = 1

    if(bit!=bitTransmitted):
        count +=1

probabilityOfFailure = count/100000
print('The probability of transmitted bit being received incorrectly is %s' %probabilityOfFailure)
