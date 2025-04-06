import numpy as np

def dice_score(y_true, y_pred):
    if np.sum(y_true) == 0 or np.sum(y_pred) == 0:
        return 0.
    numerator = 2 * np.sum([1 if ((i == j) and i == 1) else 0 for i, j in zip(y_true, y_pred)])
    denominator = np.sum(y_true) + np.sum(y_pred)
    return round(numerator/denominator, 3)