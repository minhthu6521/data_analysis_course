import pytest
import numpy as np
from rows_and_cols import get_columns, get_rows


@pytest.mark.parametrize('array, rows, columns', [
    (np.array([[5, 0, 3, 3],
               [7, 9, 3, 5],
               [2, 4, 7, 6],
               [8, 8, 1, 6]]),
    [np.array([5, 0, 3, 3]), np.array([7, 9, 3, 5]),
           np.array([2, 4, 7, 6]), np.array([8, 8, 1, 6])],
    [np.array([5, 7, 2, 8]), np.array([0, 9, 4, 8]), np.array([3, 3, 7, 1]), np.array([3, 5, 6, 6])]),
    (np.array([[1, 5, 7], [0, 0, 0], [22, 6, 8], [9, 1, 0]]),
    [np.array([1, 5, 7]), np.array([0, 0, 0]), np.array([22, 6, 8]), np.array([9, 1, 0])], 
    [np.array([ 1,  0, 22,  9]), np.array([5, 0, 6, 1]), np.array([7, 0, 8, 0])])
])
def test_rows_and_columns(array, rows, columns):
    assert np.array_equal(get_columns(array), columns) is True
    assert np.array_equal(get_rows(array), rows) is True
