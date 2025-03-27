import numpy as np

def divide_on_feature(X, feature_i, threshold):
    split_a, split_b = [], []
    for index, sample in enumerate(X):
        if sample[feature_i] >= threshold:
            split_a.append(index)
        else:
            split_b.append(index)
    return X[split_a], X[split_b]