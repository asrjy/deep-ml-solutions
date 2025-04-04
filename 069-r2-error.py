import numpy as np

def r_squared(y_true, y_pred):
    n = len(y_true)
    ssr = 0
    sst = 0
    y_mean = np.mean(y_true)
    for i in range(n):
        ssr += (y_true[i] - y_pred[i])**2
        sst += (y_true[i] - y_mean)**2
    r2 = 1 - (ssr/sst)
    return r2