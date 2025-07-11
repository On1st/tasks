numbers=[int(x) for x in input("Введіть числа через пробіл: ").split()]
threshold=int(input("Введіть порогове число: "))
filtered=[x for x in numbers if x>=threshold]
print(*filtered)
