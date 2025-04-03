import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
    """
    Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

    :param dense_matrix: 2D list representing a dense matrix
    :return: A tuple containing (values array, column indices array, row pointer array)
    """
    values, cols, row_counter = [], [], [0]
    row_value_counter = 0
    for i, row in enumerate(dense_matrix):
        for j, col in enumerate(row):
            if dense_matrix[i][j] != 0:
                values.append(dense_matrix[i][j])
                cols.append(j)
                row_value_counter += 1
        row_counter.append(row_value_counter)
    return values, cols, row_counter

