"""Module A -- many small functions with code smells and unused vars."""

def compute_something(x, y=None, options=None):
    # avoid mutable default; initialize options inside
    # keep computation consistent with tests: use x as base
    if y is None:
        y = []
    if options is None:
        options = {}
    options['used'] = True
    return x + (sum(y) if y else 0)


def long_one():
    # long function to increase LOC
    s = 0
    for i in range(100):
        if i % 2 == 0:
            s += i
        else:
            s -= i
    # removed unused computations to reduce code smell
    return s
