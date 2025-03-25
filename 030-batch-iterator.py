import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    indices = list(range(len(X)))
    indices = [indices[i:i+batch_size] for i in range(0, len(X), batch_size)]
    if len(y) >= 1:
        return ([(X[index], y[index]) for index in indices])
    else:
        return ([X[index] for index in indices])

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2
print(batch_iterator(X, y, batch_size))

