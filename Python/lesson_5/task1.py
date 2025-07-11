user_input = input("Введіть рядок: ")

letters = sum(a.isalpha() for a in user_input)
digits = sum(b.isdigit() for b in user_input)

print("Кількість букв:", letters)
print("Кількість цифр:", digits)
