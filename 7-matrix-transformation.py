import numpy as np

def get_det_2d(A):
	return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	if (len(T) != len(T[0])) or (get_det_2d(T) == 0) or (len(S) != len(S[0])) or (get_det_2d(S) == 0):
		return -1
	T_inv = np.linalg.inv(T)
	T_inv_A = np.matmul(T_inv, A)
	transformed_matrix = np.matmul(T_inv_A, S)
	return transformed_matrix