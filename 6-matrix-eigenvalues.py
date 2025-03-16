def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trace = 0
	for i, row in enumerate(matrix):
		trace += row[i]
	det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
	eigenvalues = [(trace + (trace**2 - 4 * det)**0.5)/2, (trace - (trace**2 - 4 * det)**0.5)/2]
	eigenvalues.sort(reverse=True)
	return eigenvalues