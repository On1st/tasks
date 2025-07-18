user_input = input("Введіть рядок: ")
words = user_input.split()
max_word = ""
max_length = 0
for word in words:
    if len(word) > max_length:
        max_word = word
        max_length = len(word)
print("Найдовше слово:", max_word)

