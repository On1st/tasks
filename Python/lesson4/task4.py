first=int(input("Enter your first number: "))
second=int(input("Enter your second number: "))
step = int(input("Enter the step value: "))
option = int(input("Choose an option 1: Print all numbers, 2: Print in reverse: "))
if option == 1:
    print("All numbers in range:")
    for i in range(first, second + 1, step):
        print(i, end=" ")
elif option == 2:
    print("All numbers in range in reverse order:")
    for i in range(second, first - 1, -step):
        print(i, end=" ")
else:
    print("Invalid option selected.")