import math
def problem1(a,b,c,d):
    input = [a,b,c,d]
    lowestInt = a
    highestInt = a
    for i in range(len(input)):
        if(i == 0):
            continue
        if(input[i]<lowestInt):
            lowestInt = input[i]
        if(input[i] > highestInt):
            highestInt = input[i]
    return highestInt - lowestInt


def problem2(x):
    numsSaid = 0
    lastNum = 0
    while(numsSaid < 4):
        lastNum+=1
        if(not(lastNum % 3==0 or lastNum % 5==0)):
            numsSaid+=1
    print(lastNum)
    return lastNum

def problem3():

