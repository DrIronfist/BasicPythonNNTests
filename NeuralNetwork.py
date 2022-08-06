from networkMath import *
from numpy import random

class Data:
    def __init__(self, inputCount, outputCount, layerCount, nodeCount):
        self.ic = inputCount
        self.oc = outputCount
        self.lc = layerCount
        self.nc = nodeCount


class Node:
    def __init__(self, inputcount):
        self.weights = [random.rand() for i in range(inputcount)]
        # for i in range(inputcount):
        #     self.weights.append( random.rand(2) - 1)

        self.bias = random.rand()*10 - 5

    def calculate(self, inputVector):
        activationNum = dotVectors(inputVector, self.weights)
        activationNum += self.bias
        return sigmoid(activationNum)


class Layer:
    def __init__(self, nodeCount, inputCount):
        self.nodeCount = nodeCount
        self.inputCount = inputCount
        self.nodes = [Node(0)] * nodeCount
        for i in range(self.nodeCount):
            self.nodes[i] = Node(self.inputCount)

    def calculate(self, inputVector):
        outputVector = [0] * self.nodeCount
        for i in range(self.nodeCount):
            outputVector[i] = self.nodes[i].calculate(inputVector)
        return outputVector


class Network:
    def __init__(self, data):
        previousNodeCount = data.ic
        self.layers = []
        for i in range(data.lc):
            self.layers.append(Layer(data.nc, previousNodeCount))
            previousNodeCount = data.nc
        self.layers.append(Layer(data.oc,previousNodeCount))
    def calculate(self, inputVector):
        currentInput = inputVector
        for i in range(len(self.layers)):
            currentInput = self.layers[i].calculate(currentInput)
        return currentInput
