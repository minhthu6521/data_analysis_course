import numpy as np

def get_row_vectors(arr):
    arr = np.matrix(arr)
    shape = np.shape(arr)[0]
    d = np.split(arr, shape)
    return d


def get_column_vectors(arr):
    arr = np.matrix(arr)
    shape = np.shape(arr)[1] 
    d = np.split(arr, shape, axis=1)
    return d
    
