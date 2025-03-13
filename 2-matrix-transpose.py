def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    transposed_mat = []
    row = []
    for j in range(len(a[0])):
        for i in range(len(a)):
            row.append(a[i][j])
        transposed_mat.append(row)
        row = []
    return transposed_mat

print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))