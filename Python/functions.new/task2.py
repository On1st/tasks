def list_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
print(list_product([1, 2, 3, 4]))