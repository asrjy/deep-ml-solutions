from collections import Counter

def confusion_matrix(data):
    tp, tn, fp, fn = 0, 0, 0, 0
    for pair in data:
        if (pair[0] == pair[1]):
            if pair[0] == 1:
                tp += 1
            else:
                tn += 1
        else:
            if pair[0] == 1:
                fn += 1
            else:
                fp += 1
    return [[tp, fn], [fp, tn]]