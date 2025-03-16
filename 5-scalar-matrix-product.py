def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result = [[i * scalar for i in row] for row in matrix]
	return result