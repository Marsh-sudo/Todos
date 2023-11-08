import pytest
import source.shapes as shapes


@pytest.mark.parametrize("side_length, expected_area", [(4,16), (5,25), (10,100)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area



@pytest.mark.parametrize("side_length, expected_perimeter", [(4,16), (3,12), (5,20)])
def test_multiple_perimeter(side_length,expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter