def det_2d(matrix):
    return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

def get_sub_mat(matrix, position):
    sub_mat = []
    for i in range(1, len(matrix)):
        temp_row = []
        for j in range(len(matrix[0])):
            if j != position[1]:
                temp_row.append(matrix[i][j])
        sub_mat.append(temp_row)
    return sub_mat

def nd_det(matrix):
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return det_2d(matrix)
    
    value = 0
    for i in range(len(matrix[0])):
        sub_mat = get_sub_mat(matrix, [0, i])
        sign = (-1) ** i
        value += sign * matrix[0][i] * nd_det(sub_mat)
    
    return value

def determinant_4x4(matrix):
    return nd_det(matrix)
