import numpy as np

def rmse(y_true, y_pred):
    rmse = np.sum((y_true-y_pred)**2)
    return round((rmse/y_true.size)**0.5, 3)
