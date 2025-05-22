import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
    m = np.matrix(a).shape[1]
    n = np.matrix(b).shape[1]

    # print(np.matrix(a).shape)
    # print(n)
    
    if m!=n:
        return -1

    # return np.dot(a,b)

    res = []
    for i in range(0,np.matrix(a).shape[0]):
        temp = 0
        for j in range(0,m):
            temp += a[i][j] * b[j]
        res.append(temp)
    return res
