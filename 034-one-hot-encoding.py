import numpy as np

def to_categorical(x, n_col=None):
    base_array = [0 for i in range(max(x) + 1)]
    cat_list = []
    for val in x:
        base_array[val] = 1
        cat_list.append(base_array)
        base_array = [0 for i in range(max(x) + 1)]
    return cat_list

x = np.array([0, 1, 2, 1, 0])
output = to_categorical(x)
print(output)