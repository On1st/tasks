def product_list(lst):
    prod = 1
    for n in lst:
        prod *= n
    return prod

print(product_list([1, 2, 3, 4]))
print(product_list([5, 6, 7]))
