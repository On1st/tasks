import math
import random

# ------------------ РІВЕНЬ 1 ------------------

# Завдання 1
print("=== Завдання 1 ===")
try:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    result = num1 / num2
    print(f"Результат ділення: {result:.2f}")
except ValueError:
    print("Помилка: введено нечислове значення!")
except ZeroDivisionError:
    print("Помилка: ділення на нуль неможливе!")
finally:
    print("Операцію завершено.\n")


# Завдання 2
print("=== Завдання 2 ===")
numbers = [10, 20, 30, 40, 50]
try:
    index = int(input("Введіть індекс елемента (0–4): "))
    print(f"Елемент за індексом {index}: {numbers[index]}")
except ValueError:
    print("Помилка: потрібно ввести ціле число!")
except IndexError:
    print("Помилка: індекс виходить за межі списку!")
finally:
    print("Операцію завершено.\n")


# ------------------ РІВЕНЬ 2 ------------------

# Завдання 3
print("=== Завдання 3 ===")
try:
    sales_input = input("Введіть дані про продажі через пробіл: ")
    sales = [float(x) for x in sales_input.split()]
    total = sum(sales)
    print(f"Загальна сума продажів: {total:.2f}")
except ValueError:
    print("Помилка: введено некоректні дані!")
finally:
    print("Обробку завершено.\n")


# Завдання 4
print("=== Завдання 4 ===")
try:
    num = float(input("Введіть число для обчислення квадратного кореня: "))
    if num < 0:
        raise Exception("Не можна обчислити квадратний корінь від'ємного числа")
    result = math.sqrt(num)
    print(f"Квадратний корінь з {num} = {result:.3f}")
except ValueError:
    print("Помилка: введено нечислове значення!")
except Exception as e:
    print("Помилка:", e)
finally:
    print("Обчислення завершено.\n")


# ------------------ РІВЕНЬ 3 ------------------

# Завдання 5
print("=== Завдання 5 ===")
try:
    data = input("Введіть товар у форматі: назва, ціна, кількість\n→ ")
    parts = [x.strip() for x in data.split(",")]

    if len(parts) != 3:
        raise Exception("Невірний формат введення. Має бути: назва, ціна, кількість")

    name = parts[0]
    price = float(parts[1])
    quantity = int(parts[2])

    print(f"Товар: {name}, Ціна: {price:.2f}, Кількість: {quantity}, Всього: {price * quantity:.2f}")

except ValueError:
    print("Помилка: ціна або кількість введені некоректно!")
except Exception as e:
    print("Помилка:", e)
finally:
    print("Парсинг завершено.\n")


# Завдання 6
print("=== Завдання 6 ===")

def connect_to_server():
    if random.choice([True, False]):
        return "Підключення успішне!"
    else:
        raise ConnectionError("Помилка підключення")

try:
    message = connect_to_server()
    print(message)
except ConnectionError:
    print("Не вдалося підключитися до сервера.")
finally:
    print("Спробу завершено.")
