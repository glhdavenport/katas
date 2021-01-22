from ..super_power import super_power
import pytest
# Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

# Example 1:
# Input: a = 2, b = [3]
# Output: 8

# Example 2:
# Input: a = 2, b = [1,0]
# Output: 1024

# Example 3:
# Input: a = 1, b = [4,3,3,8,5,2]
# Output: 1

# Example 4:
# Input: a = 2147483647, b = [2,0,0]
# Output: 1198
 
# Constraints:

# 1 <= a <= 2**31 - 1
# 1 <= b.length <= 2000 # TODO optimize code so that it can handle this
# 0 <= b[i] <= 9
# b doesn't contain leading zeros.

def test_super_power_example_1():
    # Given
    a = 2
    b = [3]
    
    actual = super_power(a, b)
    expected = 8 
    assert actual == expected

def test_super_power_example_2():
    # Given
    a = 2
    b = [1,0]
    
    actual = super_power(a, b)
    expected = 1024 
    assert actual == expected

def test_super_power_example_3():
    # Given
    a = 1
    b = [4,3,3,8,5,2]
    
    actual = super_power(a, b)
    expected = 1
    assert actual == expected

def test_super_power_example_4():
    # Given
    a = 2147483647
    b = [2,0,0]
    
    actual = super_power(a, b)
    expected = 1198
    assert actual == expected


def test_a_is_in_range_too_big():
    # Given
    a = 2**32
    b = [1,0,1]

    with pytest.raises(ValueError) as actual_error:
        super_power(a,b)
    
    assert actual_error.type is ValueError

def test_a_is_in_range_too_small():
    # Given
    a = 0
    b = [1,0,1]

    with pytest.raises(ValueError) as actual_error:
        super_power(a,b)
    
    assert actual_error.type is ValueError

def test_b_is_in_range_too_big():
    # 1 <= b.length <= 6
    # Given
    a = 5
    b = [1]*7

    with pytest.raises(ValueError) as actual_error:
        super_power(a,b)
    
    assert actual_error.type is ValueError
