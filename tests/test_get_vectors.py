import pytest
import numpy as np
from get_vectors import get_column_vectors, get_row_vectors


@pytest.mark.parametrize('array, rows, columns', [
    ("5 0 3; 3 7 9",
     [[[5, 0, 3]], [[3, 7, 9]]],
     [[[5],
       [3]],
      [[0],
       [7]],
      [[3],
       [9]]])
])
def test_get_vectors(array, rows, columns):
    assert np.array_equal(get_row_vectors(array), rows) is True
    assert np.array_equal(get_column_vectors(array), columns) is True
