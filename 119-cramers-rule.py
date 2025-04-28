import numpy as np

def cramers_rule(A, b):
    A = np.array(A)
    if A.shape[0] != A.shape[1]: 
        return -1
    det_A = np.linalg.det(A)
    if det_A == 0:
        return -1
    solution = []
    for i in range(A.shape[1]):
        Ai = A.copy()
        Ai[:, i] = b
        xi = round(np.linalg.det(Ai)/det_A, 4)
        solution.append(xi)
    return solution