def monster(x):
    # Simplified logic to reduce cognitive complexity
    total = sum((i * x if i < 10 else i) for i in range(200))
    # minimal post-processing
    return int(total)
