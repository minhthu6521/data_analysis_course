'''
Create function get_row_vectors that returns a list of rows from the input array of shape (n,m), but this time the rows must have shape (1,m). Similarly, create function get_columns_vectors that returns a list of columns (each having shape (n,1)) of the input matrix .
'''
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
    
