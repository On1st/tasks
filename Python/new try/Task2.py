def print_even_numbers(start, end):
    print(f"Парні числа між {start} і {end}:")
    for num in range(start + 1, end):
        if num % 2 == 0:
            print(num, end=' ')
    print()  # Для переносу рядка після виводу
