while True:
    number = int(input("Enter a number: "))

    if number == 7:
        print("Good bye!")
        break
    elif number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")
    print("Try again")