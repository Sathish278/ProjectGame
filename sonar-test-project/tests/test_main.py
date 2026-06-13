from main import add, sum_values


def test_add():
    assert add(2, 3) == 5


def test_sum_values():
    assert sum_values([1, 2, 3]) == 6
