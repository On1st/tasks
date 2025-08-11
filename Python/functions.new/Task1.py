def range_sum(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))
print(range_sum(25, 5))