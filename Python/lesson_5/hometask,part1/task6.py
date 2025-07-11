user_input = input("Введіть текст: ")
words = user_input.split()
reversed_words = words[::-1]
result = ' '.join(reversed_words)
print("Результат:", result)