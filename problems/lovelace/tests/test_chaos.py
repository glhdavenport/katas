import pytest
from ..chaos import logistic_map

# Test case 2:
# Input: r = 2
# Output: [0.5, 0.5, 0.5, ⋯, 0.5, 0.5, 0.5]

def test_rate_2_gives_list_of_constant_population():
    given = 2
    expected = [0.5] * 51
    actual = logistic_map(given)
    assert expected == actual

# Test case 1:
# Input: r = 2.81
# Output: [0.500000, 0.702500, 0.587272, ⋯, 0.644125, 0.644130, 0.644126]

def test_rate_slightly_above_2_gives_convergent_population():
    given = 2.81
    expected_first = [0.5, 0.7025, 0.587272]
    expected_last = [0.644125, 0.644130, 0.644126]
    actual = logistic_map(given)
    actual_first = actual[:3]
    actual_last = actual[-3:]
    for index, expected_value in enumerate(expected_first):
        assert expected_value == pytest.approx(actual_first[index], 0.000001)
     
    for index, expected_value in enumerate(expected_last):
        assert expected_value == pytest.approx(actual_last[index], 0.000001)

# Test case 3:
# Input: r = 3.88
# Output: [0.5, 0.97, 0.112908, ⋯, 0.940932, 0.215644, 0.656271]

def test_rate_way_above_2_gives_divergent_population():
    given = 3.88
    expected_first = [0.5, 0.97, 0.112908]
    expected_last = [0.940932, 0.215644, 0.656271]
    actual = logistic_map(given)
    actual_first = actual[:3]
    actual_last = actual[-3:]
    for index, expected_value in enumerate(expected_first):
        assert expected_value == pytest.approx(actual_first[index], 0.00001)
     
    for index, expected_value in enumerate(expected_last):
        assert expected_value == pytest.approx(actual_last[index], 0.00001)