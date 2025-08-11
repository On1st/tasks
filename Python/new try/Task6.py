def is_palindrome(number):
    number_str = str(abs(number))  # Перетворюємо число в рядок (без знаку мінус)
    return number_str == number_str[::-1]
