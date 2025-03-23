import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float):
    forward_pass = []
    temp = 0
    for feature in features:
        for i in range(len(weights)):
            temp += (feature[i] * weights[i]) 
        temp += bias
        forward_pass.append(round(1/(1 + math.exp(-temp)), 4))
        temp = 0

    mse = round(sum([(labels[i] - forward_pass[i])**2 for i in range(len(labels))])/len(labels), 4)

    return (forward_pass, mse)

features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]]
labels = [0, 1, 0]
weights = [0.7, -0.4]
bias = -0.1

single_neuron_model(features, labels, weights, bias)