import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	if new_shape[0] * new_shape[1] != len(a) * len(a[0]):
		return []
	else:
		flat_a = np.ravel(np.array(a))
		n_cols = new_shape[1]
		temp = []
		reshaped_matrix = []
		for i in range(new_shape[0]):
			for j in range(new_shape[1]):
				temp.append(flat_a[(n_cols * i) + j])
			reshaped_matrix.append(temp)
			temp = []
	return reshaped_matrix