"""
Ajay Kc
013213328
EE 381
Project 1 Part 1

The program counts the number of times it takes to roll a 7 with two dices and displays the probability mass function
"""

import random as rand
import numpy as np
import matplotlib.pyplot as plt


def roll_Seven():

    count = 1

    while(True):
        die_One = rand.randint(1,7)
        die_Two = rand.randint(1,7)
        sum_Dice = die_One + die_Two

        if(sum_Dice==7):
            break
        else:
            count +=1

    return count

def make_Figure(list):
    b = range(1,27)
    h1, bin_edges = np.histogram(list, bins=b)
    b1 = bin_edges[0:25]

    figure_One = plt.figure(1)
    p1 = h1/100000
    sum = p1.sum()
    plt.xticks(b1)
    plt.stem(b1,p1)
    plt.title('Stem plot - Number of rolls needed to get a "7" - Probability mass function')
    plt.xlabel('Number of rolls needed to get a "7"')
    plt.ylabel('Frequency')

    plt.show()


list = []
for i in range(0,100000):
    number = roll_Seven()
    if(number <=25):
        list.append(number)

make_Figure(list)
