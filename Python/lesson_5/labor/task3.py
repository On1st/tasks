user_input = input("Введіть рядок: ")

reversed_str = ""
i = len(user_input) - 1
while i >= 0:
    reversed_str += user_input[i]
    i -= 1

print("Перевернутий рядок:", reversed_str)
