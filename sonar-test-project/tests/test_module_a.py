from module_a import compute_something


def test_compute_something():
    assert compute_something(2, [1, 2]) == 5
