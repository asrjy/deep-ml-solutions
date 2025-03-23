import numpy as np 
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    C = np.array(C) 
    B = np.array(B)
    C_inv = np.linalg.inv(C)
    P = C_inv@B   
    return P