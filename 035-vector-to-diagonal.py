import numpy as np

def make_diagonal(x):
    base_matrix = [[0 for i in range(len(x))] for j in range(len(x))]
    for i in range(len(x)):
        base_matrix[i][i] = x[i]
    return base_matrix

x = np.array([1, 2, 3])
output = make_diagonal(x)
print(output)