import math
def dotVectors(v1, v2):
    sum = 0
    for i in range(len(v1)):
        sum += v1[i]*v2[i]
    return sum
def sigmoid(x):
    return 1/(1+math.exp(-x))