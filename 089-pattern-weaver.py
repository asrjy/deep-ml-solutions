import numpy as np

def softmax(values):
    values = np.array(values)
    return np.exp(values)/np.sum(np.exp(values))

def pattern_weaver(n, crystal_values, dimension):
    scores = []
    for i in range(n):
        temp = []
        for j in crystal_values:
            temp.append((crystal_values[i] * j)/np.sqrt(dimension))
        temp = softmax(temp)
        scores.append(round(sum([temp[i] * crystal_values[i] for i in range(n)]), 4))
    return scores