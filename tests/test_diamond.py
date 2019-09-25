import pytest
from diamond import diamond
import numpy as np


@pytest.mark.parametrize('len, expected', [
    (3, "0 0 1 0 0; 0 1 0 1 0; 1 0 0 0 1; 0 1 0 1 0; 0 0 1 0 0"),
    (1, [[1]])
])
def test_diamond(len, expected):
    assert np.array_equal(diamond(len), expected) is True
