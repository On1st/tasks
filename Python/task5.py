a=int(input("Enter your first mark(from one to five):"))
b=int(input("Enter your second mark(from one to five):"))
c=int(input("Enter your third mark(from one to five):"))
d=int(input("Enter your fourth mark(from one to five):"))
if 1<a>5 or 1<b>5 or 1<c>5 or 1<d>5:
    print("You have entered an invalid mark")
elif a<3 or b<3 or c<3 or d<3:
    print("You cannot be admitted to the exam")
elif a>=4 and b>=4 and c>=4 and d>=4:
    print ("You are admitted to the exam with honors:")
else:
    print("You are admitted to the exam")