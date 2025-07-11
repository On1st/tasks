user_input = input("Введіть текст: ")
chars_to_remove = input("Введіть набір символів (без пробілів): ")
filter_set = set(chars_to_remove)
words = user_input.split()
filtered_words = [word for word in words if not any(c in filter_set for c in word)]
result = ' '.join(filtered_words)
print("Результат:", result)