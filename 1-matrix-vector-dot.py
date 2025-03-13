def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(a[0]) != len(b):
		return -1
	else:
		matrix_dot_vector_val = []
		temp_val = 0
		for i in a:
			for j in range(len(i)):
				temp_val += i[j] * b[j]
			matrix_dot_vector_val.append(temp_val)
			temp_val = 0
	return matrix_dot_vector_val

print(matrix_dot_vector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]))