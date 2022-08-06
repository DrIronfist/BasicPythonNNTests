import numpy as np
import matplotlib.pyplot as plt

#define the sigmoid function
def sigmoid(x):
    return 1/(1+np.exp(-x))

#define the derivative of the sigmoid function
def deriv_sigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))

#define the stochastic gradient descent function
def stochastic_gradient_descent(x,y):

    #initialize the weight and bias with 0
    w=0
    b=0

    #set the learning rate to 0.1
    lr=0.1

    #set the number of epochs to 100000
    epochs=100000

    #initialize an empty list to store the cost after each epoch
    cost_history=[]

    #run the loop for the specified number of epochs
    for i in range(epochs):

        #get a random index from the length of x
        rand_ind=np.random.randint(len(x))

        #get the x value at the random index and y value at the random index
        xi=x[rand_ind]
        yi=y[rand_ind]

        #calculate the z value using w and b values
        z=np.dot(w,xi)+b

        #calculate the predicted value using sigmoid function
        pred=sigmoid(z)

        #calculate the cost using yi and pred values
        cost=(-yi*np.log(pred))-((1-yi)*np.log(1-pred))

        #calculate the derivative of cost with respect to w and b values
        dcost_dw=-xi*(yi-pred)
        dcost_db=-(yi-pred)

        #update the weight and bias values using gradient descent algorithm
        w=w-lr*dcost_dw
        b=b-lr*dcost_db

        #append the cost to cost history list after each epoch
        cost_history.append(cost)

    #return the weight, bias and cost history list
    return w,b,cost_history
