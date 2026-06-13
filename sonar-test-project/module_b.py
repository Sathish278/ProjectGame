"""Module B -- duplicates many functions from other modules to trigger duplication."""

def compute_something(x, y=None, options=None):
    # avoid mutable default and duplicate logic
    temp = x * 2
    if y is None:
        y = []
    if options is None:
        options = {}
    options['used'] = True
    total = temp + (sum(y) if y else 0)
    return total


def long_one():
    # duplicated long function
    s = 0
    for i in range(100):
        if i % 3 == 0:
            s += i
        elif i % 5 == 0:
            s += i
        else:
            s -= i
    return s
