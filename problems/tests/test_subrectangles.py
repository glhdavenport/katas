import pytest
from ..subrectangles import SubrectangleQueries

@pytest.fixture()
def rectangle():
    return [
        [0,1,2],
        [3,4,5],
        [6,7,8]
    ]

@pytest.fixture()
def leet_rectangle():
    return [
        [1,2,1],
        [4,3,4],
        [3,2,1],
        [1,1,1]
    ]


def test_rectangle_is_a_rectangle(rectangle):
    given = SubrectangleQueries(rectangle)
    expected = True 
    actual = given.is_valid()
    
    assert expected == actual


def test_non_rectangle_is_not_a_rectangle():
    given = SubrectangleQueries([
                [0],
                [3,4],
                [6,7,8]
            ])
    expected = False 
    actual = given.is_valid()
    
    assert expected == actual


def test_correct_value_is_returned_from_get_value(rectangle):
    rectangle = SubrectangleQueries(rectangle) 
    given_x, given_y = 1, 2
    actual = rectangle.get_value(given_x, given_y)
    expected = 5
    assert expected == actual


def test_update_subrectangle_updates_the_first_point(rectangle):
    rectangle = SubrectangleQueries(rectangle) 
    new_value = 5
    given_x1, given_y1 = 0, 0
    given_x2, given_y2 = 2, 2

    rectangle.update_subrectangle(given_x1, given_y1, given_x2, given_y2, new_value)

    actual = rectangle.get_value(given_x1, given_y1)

    assert actual == new_value


def test_update_subrectangle_does_not_update_outside_point(rectangle):
    rectangle = SubrectangleQueries(rectangle) 
    new_value = 5
    given_x1, given_y1 = 0, 0
    given_x2, given_y2 = 1, 1
    outer_x, outer_y = 2, 0

    rectangle.update_subrectangle(given_x1, given_y1, given_x2, given_y2, new_value)

    actual = rectangle.get_value(outer_x, outer_y)

    assert actual != new_value

def test_leetcode_get_value(leet_rectangle):
    #  subrectangleQueries.getValue(0, 2); // return 1
    rectangle = SubrectangleQueries(leet_rectangle)
    actual = rectangle.get_value(0, 2)
    assert actual == 1

def test_leetcode_update_subrectangle(leet_rectangle):
    # subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5);
    # // After this update the rectangle looks like:
    # // 5 5 5
    # // 5 5 5
    # // 5 5 5
    # // 5 5 5
    # subrectangleQueries.getValue(0, 2); // return 5
    # subrectangleQueries.getValue(3, 1); // return 5 
    rectangle = SubrectangleQueries(leet_rectangle)
    rectangle.update_subrectangle(0, 0, 3, 2, 5)
    actual1 = rectangle.get_value(0, 2)
    actual2 = rectangle.get_value(3, 1)
    assert actual1 == 5
    assert actual2 == 5
