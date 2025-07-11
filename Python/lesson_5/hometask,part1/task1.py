text = input("Введіть текст: ")
count = 0
for i in range(1, len(text)):
    if text[i-1] in '.!?':
        if i < len(text) and text[i].isupper():
            count += 1

print("Орієнтовна кількість речень:", count)