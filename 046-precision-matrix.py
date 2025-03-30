import numpy as np
def precision(y_true, y_pred):
    tp = 0
    fp = 0
    for i in range(len(y_true)):
        if (y_true[i] == 1) & (y_pred[i] == 1):
            tp += 1
        elif (y_true[i] == 0) & (y_pred[i] == 1):
            fp += 1
    return (tp)/(tp + fp)
