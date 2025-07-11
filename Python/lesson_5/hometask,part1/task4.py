user_input = input("Введіть рядок: ")
char1 = input("Перший символ: ")
char2 = input("Другий символ: ")
start = user_input.find(char1)
end = user_input.find(char2)
if start != -1 and end != -1 and start < end:
    result = user_input[:start] + user_input[end+1:]
else:
    result = user_input
print("Результат:", result)
