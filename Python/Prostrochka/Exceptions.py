print "---------------------Task 1----------------------"
before = int(input("Enter price before discount: "))
discount = int(input("Enter discount percentage: "))
try:
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")
    final_price = before - (before * discount / 100)
    print("Final price after discount:", final_price)
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Thank you for using our discount calculator!")

print "\n---------------------Task 2----------------------"
dollars = input("Enter amount in dollars: ")
euros = input("Enter amount in euros: ")
try:
    dollars = float(dollars)
    euros = float(euros)
    if dollars < 0 or euros < 0:
        raise ValueError("Amounts must be non-negative")
   sum_in_euros = dollars * 0.85 + euros
    print("Total amount in euros:", sum_in_euros)
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Thank you for using our currency converter!")
print "\n---------------------Task 3----------------------"
try:
    grades_input = input("Enter grades separated by spaces: ")
    grades = list(map(int, grades_input.split()))
    if not grades:
        raise ValueError("No grades entered")
    if any(grade < 0 or grade > 100 for grade in grades):
        raise ValueError("Grades must be between 0 and 100")
    average = sum(grades) / len(grades)
    print("Average grade:", average)
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Thank you for using our grade calculator!")
except ZeroDivisionError:
    print("Error: No grades entered to calculate average.")
print "\n---------------------Task 4----------------------"
ballance = 1000
try:
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    if amount > ballance:
        raise ValueError("Insufficient funds")
    ballance -= amount
    print("Withdrawal successful. New balance:", ballance)
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Thank you for using our ATM service!")
print "\n---------------------Task 5----------------------"
number_of_reservations = input("Enter your reservation: ")
try:
    if not (number_of_reservations.startswith("ORD") and number_of_reservations [3:].isdigit() and len(number_of_reservations) == 8):
        raise ValueError("Invalid reservation format. It should be 'ORD' followed by 5 digits.")
                         print("Reservation accepted:", number_of_reservations)
    else:
        print("Reservation accepted:", number_of_reservations)
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Thank you for using our reservation system!")

print "\n---------------------Task 6----------------------"
numbers = int(input("Enter a list of numbers separated by spaces: "))
try:
    num_list = list(map(int, numbers.split()))
    if not num_list:
        raise ValueError("No numbers entered")
    average = sum(num_list) / len(num_list)
    above_average = [num for num in num_list if num > average]
    print("Numbers above average:", above_average)
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
except ZeroDivisionError:
    print("Error: No numbers entered to calculate average.")
finally:
    print("Thank you for using our number analyzer!")
    