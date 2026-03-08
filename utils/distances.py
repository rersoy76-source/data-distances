def minkowski(a, b, p):
    if len(a) != len(b):
        raise ValueError("Inputs must have the same length")

    total = 0
    for x, y in zip(a, b):
        total += abs(x - y) ** p

    return total ** (1 / p)


def manhattan(a, b):
    return minkowski(a, b, 1)


def euclidean(a, b):
    return minkowski(a, b, 2)