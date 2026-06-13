def append_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst


class Greeter:
    def greet(self, name):
        return f"Hello, {name}!"


def buggy_try(x):
    # catch specific exception instead of broad except
    try:
        return 10 / x
    except ZeroDivisionError:
        return None


def sum_items(items):
    total = 0
    for item in items:
        total += item
    return total


def duplicate_sum(values):
    # intentionally duplicated logic to show duplication warning
    total = 0
    for v in values:
        total += v
    return total
