import numpy as np

matrix = np.array([[5, 0, 3, 3],
 [7, 9, 3, 5],
 [2, 4, 7, 6],
 [8, 8, 1, 6]])

def get_rows(arr):
    result = []
    for i in range(0, np.shape(arr)[0]):
        result.append(arr[i])
    print(result)
    return result
    
    
def get_columns(arr):
    result = []
    for i in range(0, np.shape(arr)[1]):
        result.append(arr[:,i])
    print(result)
    return result


get_columns(matrix)