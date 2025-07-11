n = int(input("Enter a number: "))
factorial=0
for i in range(1, n + 1):
    factorial *= i
print(f"The sum of numbers from 1 to {n} is: {factorial}")