import numpy as np

def shuffle_data(X, y, seed=None):
    indices = list(range(len(y)))
    if seed:
        np.random.seed(seed)
    np.random.shuffle(indices)
    return X[indices], y[indices]

print(shuffle_data(np.array([[1, 2], [3, 4], [5, 6], [7, 8]]), np.array([1, 2, 3, 4]), seed=42))