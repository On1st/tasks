reserved_words = {"if", "else", "while", "for", "return", "def"}
user_input = input("Введіть текст: ")
words = user_input.split()
processed_words = []
for word in words:
    stripped = ''.join(char for char in word if char.isalnum())
    if stripped in reserved_words:
        word_upper = word.replace(stripped, stripped.upper())
        processed_words.append(word_upper)
    else:
        processed_words.append(word)
result = ' '.join(processed_words)
print("Змінений текст:", result)
