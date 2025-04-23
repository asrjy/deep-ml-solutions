import numpy as np

def gini_impurity(y):
    probs = {}
    for i in y:
        if i in probs.keys():
            probs[i] += 1
        else:
            probs[i] = 1
    for i in probs.keys():
        probs[i] /= len(y)
    gini_impurity = 1
    for i in probs.keys():
        gini_impurity -= probs[i]**2
    return round(gini_impurity, 3)