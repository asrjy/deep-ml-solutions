import numpy as np

def get_x1(A, x_2, x_3, b):
	return (b[0] - (A[0][1] * x_2) - (A[0][2] * x_3)) * (1/A[0][0])

def get_x2(A, x_1, x_3, b):
	return (b[1] - (A[1][0] * x_1) - (A[1][2] * x_3)) * (1/A[1][1])	

def get_x3(A, x_1, x_2, b):
	return (b[2] - (A[2][0] * x_1) - (A[2][1] * x_2)) * (1/A[2][2])

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	jacobi_solution = [0, 0, 0]
	for i in range(n):
		solution = jacobi_solution.copy()
		jacobi_solution[0] = round(get_x1(A, solution[1], solution[2], b), 4)
		jacobi_solution[1] = round(get_x2(A, solution[0], solution[2], b), 4)
		jacobi_solution[2] = round(get_x3(A, solution[0], solution[1], b), 4)

	return jacobi_solution

print(solve_jacobi(A = [[5, -2, 3], [-3, 9, 1], [2, -1, -7]], b = [-1, 2, 3], n=2))
