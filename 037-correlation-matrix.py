import numpy as np

def calculate_correlation_matrix(X, Y=None):
    X = np.asarray(X)
    if Y is not None:
        Y = np.asarray(Y)
        XY = np.hstack((X, Y))
        corr_matrix = np.corrcoef(XY.T)
        return corr_matrix[:X.shape[1], X.shape[1]:]
    else:
        return np.corrcoef(X.T)