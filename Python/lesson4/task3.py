first=int(input("Enter your first number: "))
second=int(input("Enter your second number: "))
for i in range(first, second + 1):
    if i %3==0 and i %5==0:
        print("FizzBuzz", end=" ")
    elif i %3==0:
        print("Fizz", end=" ")
    elif i %5==0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")

        