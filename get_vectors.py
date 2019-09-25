import numpy as np

def get_row_vectors(arr):
    arr = np.matrix(arr)
    shape = np.shape(arr)[1]
    return arr.reshape(1, shape)

def get_column_vectors(arr):
    arr = np.matrix(arr)
    shape = np.shape(arr)[0]
    return arr.reshape(shape, 1)