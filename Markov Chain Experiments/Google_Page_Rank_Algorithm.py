"""
Ajay Kc
013213328
EE381
Project 6 Part 2
The experiment deals with five state Markov Chain where theoretical probability is plotted and the probability of each
page being visited is calculated.
"""
import numpy as np
import matplotlib.pyplot as plt

step = 20
transition_matrix = [[0,1,0,0,0],
                     [1/2,0,1/2,0,0],
                     [1/3,1/3,0,0,1/3],
                     [1,0,0,0,0],
                     [0,1/3,1/3,1/3,0]]
v1 = [1/5,1/5,1/5,1/5,1/5]
v2 = [0,0,0,0,1]
theoretical_probability_one = np.zeros((step+1,5))
theoretical_probability_two = np.zeros((step+1,5))
theoretical_probability_one[0,:]=v1
theoretical_probability_two[0,:]=v2

def calculate_theoretical_probabilities():
    for i in range(step):
        theoretical_probability_one[i+1,:]=np.matmul(theoretical_probability_one[i,:],transition_matrix)
        theoretical_probability_two[i + 1, :] = np.matmul(theoretical_probability_two[i, :], transition_matrix)

def plotGraph(state_one,state_two,state_three,state_four,state_five,xlabel,ylabel,title):

    plt.xlabel(xlabel, fontsize=20)
    plt.ylabel(ylabel, fontsize=20)
    plt.title(title, fontsize=20)

    plt.figure(1)
    plt.plot(range(0,step+1),state_one,color='b',marker='d',linestyle='--', label='State A')
    plt.plot(range(0, step + 1), state_two, color='r', marker='H', linestyle='--', label='State B')
    plt.plot(range(0, step + 1), state_three, color='g', marker='^', linestyle='--', label='State C')
    plt.plot(range(0, step + 1), state_four, color='m', marker='*', linestyle='--', label='State D')
    plt.plot(range(0, step + 1), state_five, color='y', marker='p', linestyle='--', label='State E')
    plt.legend(loc='best')

    plt.show()



calculate_theoretical_probabilities()

plotGraph(theoretical_probability_one[:,0],theoretical_probability_one[:,1],theoretical_probability_one[:,2],
          theoretical_probability_one[:, 3],theoretical_probability_one[:,4],"Step Number","Probability",
          "Five state Markov Chain - Calculated Using the State Transition Matrix where each state has equal initial probability")


plotGraph(theoretical_probability_two[:,0],theoretical_probability_two[:,1],theoretical_probability_two[:,2],
          theoretical_probability_two[:, 3],theoretical_probability_two[:,4],"Step Number","Probability",
          "Five state Markov Chain - Calculated Using the State Transition Matrix where one site is the home page")
