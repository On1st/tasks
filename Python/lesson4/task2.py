first=int(input("Enter your first number: "))
second=int(input("Enter your second number: "))
print("All numbers in range:")
for i in range(first, second + 1):
    print(i, end=" ")
print('\nAll numbers of range in reverse order:')
for i in range(second, first - 1, -1):
    print(i, end=" ")
print("\nAll numbers of range that are divisible by 7:")
for i in range(first, second + 1):
    if i % 7 == 0:
        print(i, end=" ")
print("\nAmount of number s that are divisible by 5:")
count = 0
for i in range(first, second + 1):
    if i % 5 == 0:
        count += 1
print(count)