age=int(input("Enter your's car age(in years): "))
mileage=int(input("Enter your's car mileage(in kilometers): "))
if age < 3 and mileage < 30000:
    print("Your car is new")
elif 3 <= age < 10 and 30000 <= mileage < 100000:
    print("Your car is in good condition")
elif age >= 10 or mileage >= 100000:
    print("The car needs to be checked")
elif age < 0 or mileage < 0:
    print("You have entered an invalid value")