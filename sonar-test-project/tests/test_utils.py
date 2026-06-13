from utils import append_item, sum_items


def test_append_item():
    lst = append_item(1, None)
    assert lst == [1]


def test_sum_items():
    assert sum_items([1, 2, 3]) == 6
