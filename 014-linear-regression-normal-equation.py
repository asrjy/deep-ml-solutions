import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	x_np = np.array(X)
	x_np_t = x_np.T
	y_np = np.array(y)
	normal_equation = np.linalg.inv(x_np_t@x_np)
	normal_equation = normal_equation@(x_np_t@y)
	return np.round(normal_equation, 1)