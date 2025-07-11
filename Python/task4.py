a=int(input("Enter your first mark: "))
b=int(input("Enter your second mark: "))
c=int(input("Enter your third mark: "))
if a<=2 or b<=2 or c<=2:
    print("You have failed the exam")
elif 2<a<4 or 2<b<4 or 2<c<4:
    print("You have passed the exam")
elif a>=4 and b>=4 and c>=4:
    print("You have passed the exam well")