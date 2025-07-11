sumeven = 0
sumodd = 0
counteven = 0
countodd = 0
summultipleof9 = 0
countmultipleof9 = 0
a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
for i in range(a, b + 1):
    if i % 2 == 0:
        sumeven += i
        counteven += 1
    else:
        sumodd += i
        countodd += 1
    if i % 9 == 0:
        summultipleof9 += i
        countmultipleof9 += 1
print("Sum of even numbers:", sumeven)
print("Count of even numbers:", counteven)
print("Sum of odd numbers:", sumodd)
print("Count of odd numbers:", countodd)
print("Sum of numbers that are multiple of 9:", summultipleof9)
print("Count of numbers that are multiple of 9:", countmultipleof9)

