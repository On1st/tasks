user_input = input("Введіть список цілих чисел через пробіл: ")
numbers = [int(n) for n in user_input.split()]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Кількість парних чисел:", even_count)
print("Кількість непарних чисел:", odd_count)
