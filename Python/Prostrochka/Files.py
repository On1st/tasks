import os
from collections import Counter

# ------------------ РІВЕНЬ 1 ------------------

# Завдання 1
print("=== Завдання 1 ===")
try:
    lines = []
    for i in range(1, 4):
        line = input(f"Введіть рядок {i}: ")
        lines.append(line)

    with open("data.txt", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print("Рядки успішно записано у файл data.txt.\n")
except Exception as e:
    print("Помилка:", e)


# Завдання 2
print("=== Завдання 2 ===")
filename = "data.txt"

if os.path.exists(filename):
    print("Файл data.txt існує. Його кожен другий рядок:")
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for i in range(1, len(lines), 2):
            print(lines[i].strip())
else:
    print("Файл data.txt не знайдено.\n")

print()


# ------------------ РІВЕНЬ 2 ------------------

# Завдання 3
print("=== Завдання 3 ===")
try:
    with open("data.txt", "r", encoding="utf-8") as f_in, open("filtered.txt", "w", encoding="utf-8") as f_out:
        for line in f_in:
            if "Python" in line:
                f_out.write(line)
    print("Рядки з 'Python' збережено у файл filtered.txt.\n")
except FileNotFoundError:
    print("Помилка: файл data.txt не знайдено!\n")


# Завдання 4
print("=== Завдання 4 ===")
try:
    filename = input("Введіть ім'я файлу для очищення від цифр: ")
    with open(filename, "r", encoding="utf-8") as f_in:
        content = f_in.read()

    cleaned = ''.join(ch for ch in content if not ch.isdigit())

    with open("cleaned.txt", "w", encoding="utf-8") as f_out:
        f_out.write(cleaned)

    print("Файл очищено від цифр і збережено як cleaned.txt.\n")
except FileNotFoundError:
    print("Помилка: файл не знайдено!\n")


# ------------------ РІВЕНЬ 3 ------------------

# Завдання 5
print("=== Завдання 5 ===")
try:
    with open("log.txt", "r", encoding="utf-8") as f:
        text = f.read().lower()
        words = [word.strip('.,!?;:"()[]') for word in text.split()]
        counter = Counter(words)
        most_common = counter.most_common(10)

    with open("word_stats.txt", "w", encoding="utf-8") as f_out:
        for word, count in most_common:
            f_out.write(f"{word}: {count}\n")

    print("10 найпоширеніших слів записано у файл word_stats.txt.\n")
except FileNotFoundError:
    print("Помилка: файл log.txt не знайдено!\n")


# Завдання 6
print("=== Завдання 6 ===")
try:
    with open("data.txt", "r", encoding="utf-8") as f_in:
        lines = f_in.readlines()

    reversed_lines = lines[::-1]

    with open("reversed.txt", "w", encoding="utf-8") as f_out:
        for line in reversed_lines:
            f_out.write(line)

    print("Рядки з файлу data.txt інвертовано і збережено у reversed.txt.\n")
except FileNotFoundError:
    print("Помилка: файл data.txt не знайдено!\n")
