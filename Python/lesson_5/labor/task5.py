user_input = input("Введіть рядок: ")
word_for_search = input("Введіть слово для пошуку: ")
word_for_replace = input("Введіть слово для заміни: ")
replaced_str = user_input.replace(word_for_search, word_for_replace)
print("Рядок після заміни:", replaced_str)