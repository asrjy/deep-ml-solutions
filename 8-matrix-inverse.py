def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
	inv_det = 1/((matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]))
	a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
	inverse = [[d * inv_det, -b * inv_det], [-c * inv_det, a * inv_det]]
	inverse = [[round(i, 1) for i in row] for row in inverse]
	return inverse