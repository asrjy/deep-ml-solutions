import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	nrows, ncols = X.shape
	theta = np.zeros(ncols)
	for i in range(iterations):
		y_pred = X@theta
		error = y_pred - y
		grad = (1/nrows)*(X.T@(error))
		theta -= (alpha * grad)
	return np.round(theta, 4)