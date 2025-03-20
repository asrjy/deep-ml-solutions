import numpy as np
def feature_scaling(data):
    MIN = -9999999999
    MAX = 9999999999
    n_rows = len(data)
    means = []
    mins = [MAX for i in range(len(data[0]))]
    maxs = [MIN for i in range(len(data[0]))]
    stds = [0 for i in range(len(data[0]))]

    for i in range(len(data[0])):
        means.append(data.T[i].mean())
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] > maxs[j]:
                maxs[j] = data[i][j]
            if data[i][j] < mins[j]:
                mins[j] = data[i][j]
            stds[j] += (data[i][j] - means[j])**2
    stds = [(i/(n_rows))**0.5 for i in stds]

    standardized = []
    minmaxnormalized = []
    temp_row_standardized = []
    temp_row_minmaxnormalized = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            temp_row_standardized.append((data[i][j] - means[j])/stds[j])
            temp_row_minmaxnormalized.append((data[i][j] - mins[j])/(maxs[j] - mins[j]))
        standardized.append(temp_row_standardized)
        minmaxnormalized.append(temp_row_minmaxnormalized)
        temp_row_standardized = []
        temp_row_minmaxnormalized = []
	
    return standardized, minmaxnormalized

data = np.array([[1, 2], [3, 4], [5, 6]])
print(feature_scaling(data))