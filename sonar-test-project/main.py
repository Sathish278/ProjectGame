def add(a, b):
    return a + b


def unused_function():
    # removed unused secret to avoid code smell
    return None


def sum_values(values):
    total = 0
    for v in values:
        total += v
    return total


if __name__ == "__main__":
    print(add(2, 3))
    print(sum_values([1, 2, 3]))
