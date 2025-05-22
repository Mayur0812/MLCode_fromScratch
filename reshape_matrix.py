import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    flat_list = np.concatenate(a).tolist()
    if len(flat_list) != (new_shape[0] * new_shape[1]):
        return [ ]

    reshaped_matrix = []
    for i in range(0,new_shape[0]):
        reshaped_matrix.append(flat_list[i*new_shape[1]:(i*new_shape[1])+new_shape[1]])
	return reshaped_matrix