import pytest
from student import calculate_grade


def test_grade_s():
    assert calculate_grade(95) == "S"


def test_grade_a():
    assert calculate_grade(85) == "A"


def test_grade_b():
    assert calculate_grade(70) == "B"


def test_grade_c():
    assert calculate_grade(55) == "C"


def test_grade_d():
    assert calculate_grade(45) == "D"


def test_grade_f():
    assert calculate_grade(30) == "F"


@pytest.mark.parametrize("avg, expected", [
    (90, "S"),
    (89, "A"),
    (80, "A"),
    (79, "B"),
    (65, "B"),
    (64, "C"),
    (50, "C"),
    (49, "D"),
    (40, "D"),
    (39, "F"),
])
def test_boundary_conditions(avg, expected):
    assert calculate_grade(avg) == expected


def test_invalid_negative_marks():
    assert calculate_grade(-10) == "F"


def test_invalid_high_marks():
    assert calculate_grade(150) == "F"
