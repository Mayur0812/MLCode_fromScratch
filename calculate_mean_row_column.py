import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    matrix = np.array(matrix)
    # print(matrix.shape)
    means = []
    if mode == 'column':
        for i in range(0, matrix.shape[0]):
            sum_ = 0
            for j in range(0,matrix.shape[1]):
                sum_+=matrix[j][i]
            means.append(float(sum_/matrix.shape[0]))
    if mode =='row':
        for i in range(0,matrix.shape[0]):
            sum_ = 0
            for j in range(0,matrix.shape[1]):
                sum_+=matrix[i][j]
            means.append(float(sum_/matrix.shape[1]))
    return means

