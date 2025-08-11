import math

def factorial_list(numbers):
    return [math.factorial(n) if n >= 0 else None for n in numbers]
print(factorial_list([0, 1, 2, 3, 4, -1, 5]))