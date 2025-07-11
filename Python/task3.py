total=int(input("Enter the total amount: "))
age=int(input("Enter your age: "))
if age < 18:
    print(f"Total amount of discount:{ total * 0.1}")
    print (f"Price after discount:{total - (total * 0.1)}")
elif 18 <= age < 60:
    print(f"Total amount of discount: {total * 0.05}")
    print(f"Price after discount: {total - (total * 0.05)}")
elif age >= 60:
    print(f"Total amount of discount: {total * 0.15}")
    print(f"Price after discount: {total - (total * 0.15)}")