def count_numbers(numbers):
    even = sum(1 for n in numbers if n % 2 == 0)
    odd = len(numbers) - even
    positive = sum(1 for n in numbers if n > 0)
    negative = sum(1 for n in numbers if n < 0)
    return even, odd, positive, negative
print(count_numbers([2, 7, -1, 9, -4, 0]))