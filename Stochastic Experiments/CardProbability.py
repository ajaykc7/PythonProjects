"""
Ajay Kc
013213328
EE 381
Project 1 Part 3

The program checks the probability of getting 4 of a kind card
"""

import numpy as np

def fourOfAKind():

    #drawnCards = np.random.randint(1,53,5)
    drawnCards = np.random.permutation(52)[0:5]
    cardFaces = {}
    for i in drawnCards:
        if (i % 13 in cardFaces):
            cardFaces[i % 13] += 1
        else:
            cardFaces[i % 13] = 1

    for k, v in cardFaces.items():
        if v == 4:
            return 'Success'

    return 'Failure'


successCount = 0
for i in range(0, 100000):
    if fourOfAKind() == 'Success':
        successCount += 1

probability = successCount / 100000
print('The probability of getting a 4-of-a-kind when 5 cards are drawn %s' % (probability))
