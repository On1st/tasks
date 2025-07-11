A = float(input("Введіть число A: "))
N = int(input("Введіть ступінь N: "))
result = 1
if N > 0:
    for _ in range(N):
        result *= A
elif N == 0:
    result = 1
else:
    for _ in range(-N):
        result *= A
    result = 1 / result
print("Результат:", result)