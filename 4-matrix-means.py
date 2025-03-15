def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'column':
		means = []
		temp = 0
		for j in range(len(matrix[0])):
			for i in range(len(matrix)):
				temp += matrix[i][j]
			means.append(temp/len(matrix))
			temp = 0
	else:
		means = []
		temp = 0
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				temp += matrix[i][j]
			means.append(temp/len(matrix[0]))
			temp = 0
	return means