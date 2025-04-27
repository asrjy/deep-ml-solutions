import numpy as np

def batch_normalization(X: np.ndarray, gamma: np.ndarray, beta: np.ndarray, epsilon: float = 1e-5) -> np.ndarray:
    n_channels = X.shape[1]
    for i in range(n_channels):
        mean_temp = X[:, i, :, :].mean()
        mean_var = X[:, i, :, :].var()
        X[:, i, :, :] = (X[:, i, :, :] - mean_temp)/np.sqrt(mean_var + epsilon)

    X *= gamma
    X += beta 

    return X
    