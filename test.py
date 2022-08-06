from NeuralNetwork import *
import world_bank_data as wb
n1 = Network(Data(3, 3, 2, 4))
print(Network.calculate(n1,[2,1,3]))
print(wb.get_topics())
