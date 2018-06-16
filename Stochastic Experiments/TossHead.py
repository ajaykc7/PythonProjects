"""
Ajay Kc
013213328
EE 381
Project 1 Part 2

The program checks the number of times it takes to get 50 heads when 100 coins are tossed
"""

import numpy as np

def toss_Coin():

    coin_List = np.random.randint(0,2,100)

    count_Head = sum(coin_List)
    if(count_Head==50):
        return "Success"
    else:
        return "Fail"

count_Success = 0

for i in range(0,100000):
    if (toss_Coin()=="Success"):
        count_Success +=1

probability = count_Success/100000
print ("The probability of getting exactly 50 heads is  %s"  %(probability))


