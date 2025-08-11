def sum_in_range(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))

print(sum_in_range(5, 25))
print(sum_in_range(25, 5))
