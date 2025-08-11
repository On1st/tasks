def is_fibonacci(n):
    if n < 0:
        return False
    # Формула: n є Фібоначчі, якщо (5n²+4) або (5n²−4) — квадрат
    def is_perfect_square(x):
        return int(x**0.5)**2 == x
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

def find_fibonacci(numbers):
    return [n for n in numbers if is_fibonacci(n)]
