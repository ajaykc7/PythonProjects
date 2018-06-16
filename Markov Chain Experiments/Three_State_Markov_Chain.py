"""
Ajay Kc
013213328
EE381
Project 6 Part 1
The experiment deals with three state Markov Chain where experimental probability and theoretical probability is plotted.
"""
import numpy as np
import matplotlib.pyplot as plt

step = 15
number = 10000
transition_matrix = [[1/3,1/3,1/3],[1/2,0,1/2],[1/4,1/4,1/2]]
initial_probability = [1/4,1/2,1/4]

X = np.zeros((step+1,number), dtype = int)
S = np.zeros((step+1), dtype=int)
experimental_probability = np.zeros((step+1,3))
theoretical_probability = np.zeros((step+1,3))
theoretical_probability[0,:]=initial_probability

def simulate_markov_chain():

    probability = np.random.rand()
    state = 0
    if(probability<=initial_probability[0]):
        state = 0
    elif((probability >initial_probability[0])and(probability<=initial_probability[0]+initial_probability[1])):
        state = 1
    else:
        state = 2

    S[0]=state

    for s in range(step):
        state=S[s]
        transition_probability=np.random.rand()
        if(state == 0):
            if(transition_probability<=transition_matrix[0][0]):
                state = 0
            elif((transition_probability>transition_matrix[0][0])and(transition_probability<=transition_matrix[0][0]+transition_matrix[0][1])):
                state = 1
            else:
                state = 2
        elif(state == 1):
            if (transition_probability <= transition_matrix[1][0]):
                state = 0
            else:
                state = 2
        else:
            if (transition_probability <= transition_matrix[2][0]):
                state = 0
            elif ((transition_probability > transition_matrix[2][0]) and (transition_probability <= transition_matrix[2][1])):
                state = 1
            else:
                state = 2
        S[s+1]=state

    return S

def calculate_experimental_probabilities():
    for i in range(step+1):
        experimental_probability[i][0]=X[i,:].tolist().count(0)/number
        experimental_probability[i][1] = X[i, :].tolist().count(1)/number
        experimental_probability[i][2] = X[i, :].tolist().count(2)/number

def calculate_theoretical_probabilities():
    for i in range(step):
        theoretical_probability[i+1,:]=np.matmul(theoretical_probability[i,:],transition_matrix)

def plotGraph(state_one,state_two,state_three,xlabel,ylabel,title):

    plt.xlabel(xlabel, fontsize=20)
    plt.ylabel(ylabel, fontsize=20)
    plt.title(title, fontsize=20)

    plt.figure(1)
    plt.plot(range(0,step+1),state_one,color='b',marker='d',linestyle='--', label='State R')
    plt.plot(range(0, step + 1), state_two, color='r', marker='H', linestyle='--', label='State N')
    plt.plot(range(0, step + 1), state_three, color='g', marker='^', linestyle='--', label='State S')
    plt.legend(loc='best')

    plt.show()

for n in range(number):
    X[:,n]=simulate_markov_chain()

simulation_one = X[:,0]
simulation_two = X[:,1]

r_simulation_one=np.zeros(step+1,dtype=int)
n_simulation_one=np.zeros(step+1,dtype=int)
s_simulation_one=np.zeros(step+1,dtype=int)
r_simulation_two=np.zeros(step+1,dtype=int)
n_simulation_two=np.zeros(step+1,dtype=int)
s_simulation_two=np.zeros(step+1,dtype=int)

for i in range(step+1):
    if(simulation_one[i]==0):
        r_simulation_one[i]=1
    elif(simulation_one[i]==1):
        n_simulation_one[i]=1
    else:
        s_simulation_one[i]=1

    if (simulation_two[i] == 0):
        r_simulation_two[i] = 1
    elif (simulation_two[i] == 1):
        n_simulation_two[i] = 1
    else:
        s_simulation_two[i] = 1

calculate_experimental_probabilities()
calculate_theoretical_probabilities()

plotGraph(r_simulation_one,n_simulation_one,s_simulation_one,'Step Number','State of the Markov Chain',
          'Three-state Markov Chain: Results from a Single Simulation Run')
plotGraph(r_simulation_two,n_simulation_two,s_simulation_two,'Step Number','State of the Markov Chain',
          'Three-state Markov Chain: Results from a Single Simulation Run')
plotGraph(experimental_probability[:,0],experimental_probability[:,1],experimental_probability[:,2],'Step Number',
          'Probability','Three-state Markov Chain: Results from N=10000 Single Simulation Runs')
plotGraph(theoretical_probability[:,0],theoretical_probability[:,1],theoretical_probability[:,2],'Step Number',
          'Probability','Three-state Markov Chain: Calculated Using the State Transition Matrix')
