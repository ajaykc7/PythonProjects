"""
Ajay Kc
013213328
EE 381
Project 1 Part 3

The program checks the probability a password getting hacked
"""
import random as rand
import numpy as np
import math


def generatePassword():
    password = ""
    for i in range(0, 4):
        password = password + chr(rand.randint(97, 122))

    return password


def checkMatch(listLength):
    n = (math.pow(26, 4)) - 1
    count = 0
    for i in range(0, 1000):
        myPassword = rand.randint(0, n)
        hackerPasswordList = np.random.randint(0, n, listLength)

        if (myPassword in hackerPasswordList):
            count += 1

    return count


successOneCount = checkMatch(100000)
successTwoCount = checkMatch(1000000)
print("The probability of matching the password with hacker's list of 10^5 words %s" %(successOneCount / 1000))
print("The probability of matching the password with hacker's list of 10^6 words %s" %(successTwoCount / 1000))

print(checkMatch(340000)/1000)