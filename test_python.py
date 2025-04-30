import math


def test_filter_positive_numbers():
    numbers = [-10, 0, 3, -5, 7]
    assert list(filter(lambda x: x > 0, numbers)) == [3, 7]
    numbers = [10, 0, 3, 5, -7]
    assert list(filter(lambda x: x < 0, numbers)) == [-7]


def test_map():
    assert list(map(lambda x: x * x, [1, 2, 3])) == [1, 4, 9]
    assert list(map(len, ["cat", "elephant", "dog"])) == [3, 8, 3]
    assert list(map(lambda x: x * x, [2, 4, 3])) == [4, 16, 9]
    assert list(map(len, ["dog", "cat", "sun"])) == [3, 3, 3]

def test_sorted():
    numbers = [5, 2, 9, 1]
    assert sorted(numbers) == [1, 2, 5, 9]
    assert sorted(numbers, reverse=True) == [9, 5, 2, 1]
    numbers = [1, 2, 3, 4]
    assert sorted(numbers) == [1, 2, 3, 4]
    assert sorted(numbers, reverse=True) == [4, 3, 2, 1]


def test_pi():
    assert round(math.pi, 2) == 3.14


def test_sqrt():
    assert math.sqrt(4) == 2
    assert math.sqrt(9) == 3
    assert math.sqrt(16) == 4
    assert math.sqrt(25) == 5


def test_pow():
    assert math.pow(2, 3) == 8
    assert math.pow(5, 2) == 25
    assert math.pow(3, 2) == 9
    assert math.pow(4, 2) == 16


def test_hypot():
    # гипотенуза ( c ) равна квадратному корню из суммы
    # квадратов катетов:
    assert math.hypot(3, 4) == 5
    assert math.hypot(6, 8) == 10







