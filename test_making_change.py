import pytest

from making_change import make_change, CannotMakeChangeException

def test_making_change_default_inputs():
    '''confirm we get expected values from the default inputs for making change'''
    result = make_change(6, [1, 5, 10, 25])
    assert result in [{5: 1, 1: 1}, {1: 6}]

    result = make_change(6, [3, 4])
    assert result == {3: 2}

    result = make_change(6, [1, 3, 4])
    assert result in [{4: 1, 1: 2}, {1: 6}, {3: 2}]

    with pytest.raises(CannotMakeChangeException) as excinfo:
        result = make_change(6, [5, 7])


def test_making_change_from_unordered_inputs():

    result = make_change(6, [10, 5, 1, 25])
    assert result in [{5: 1, 1: 1}, {1: 6}]
