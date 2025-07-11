first=int(input("Enter your first number: "))
second=int(input("Enter your second number: "))
for i in range(first, second + 1):
    if i %7==0:
        print(i, end=" ")