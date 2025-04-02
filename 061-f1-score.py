import numpy as np

def f_score(y_true, y_pred, beta):
    """
    Calculate F-Score for a binary classification task. 
    :param y_true: Numpy array of true labels
    :param y_pred: Numpy array of predicted labels
    :param beta: The weight of precision in the harmonic mean
    :return: F-Score rounded to three decimal places
    """
    tp, fp, fn = 0, 0, 0
    for i in range(len(y_true)):
        if y_true[i] == 1:
            if y_pred[i] == 0:
                fn += 1
            else:
                tp += 1
        else:
            if y_pred[i] == 1:
                fp += 1
    precision = tp/(tp + fp)
    recall = tp/(tp + fn)
    beta2 = beta*beta
    f1 = (1 + beta2) * (precision * recall) / ((beta2 * precision) + recall)
    return round(f1, 3)
