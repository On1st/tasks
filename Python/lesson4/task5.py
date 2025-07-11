first=int(input("Enter your first number: "))
second=int(input("Enter your second number: "))
if second >first:
    for i in range(first, second + 1):
        if i %4==0 and i %6!=0:
            print(i, end=" ")
else:
    print("Not found", end=" ")
if second < first:
    for i in range(first, second - 1, -1):
        if i %4==0 and i %6!=0:
            print(i, end=" ")
    else:
        print("Not found", end=" ")
if second == first:
    if first %4==0 and first %6!=0:
        print(first, end=" ")
    else:
        print("Not found", end=" ")