def range_product(a, b):
    if a > b:
        a, b = b, a
    product = 1
    for num in range(a, b + 1):
        product *= num
    return product
print(range_product(3, 5))
