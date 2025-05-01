def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
    tp, tn, fp, fn = 0, 0, 0, 0
    for i in range(len(actual)):
        if actual[i] == 1:
            if actual[i] == predicted[i]:
                tp += 1
            else:
                fn += 1
        else:
            if actual[i] == predicted[i]:
                tn += 1
            else:
                fp += 1

    accuracy = (tp + tn)/(tp + tn + fp + fn)
    specificity = tn/(tn + fp)
    precision = tp/(tp + fp)
    recall = tp/(tp + fn)
    f1 = 2 * ((precision * recall)/(precision + recall))
    negativePredictive = tn/(tn + fn)
    confusion_matrix = [[tp, fn], [fp, tn]]

    return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)
