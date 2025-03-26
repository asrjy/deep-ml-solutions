import numpy as np

def accuracy_score(y_true, y_pred):
    n_samples = len(y_true)
    acc = 0
    for i in range(n_samples):
        if y_true[i] == y_pred[i]:
            acc += 1
    return acc/n_samples