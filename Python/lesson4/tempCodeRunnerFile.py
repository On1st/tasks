first=int(input("Enter your first number: "))
second=int(input("Enter your second number: "))
for i in range(first, second + 1):
    print("all numbers in range:", i, end=" ")
for j in range(second,first + 1):
    if first>second:
        print("all numbers in reverse range:", j, end=" ")
for i in range(first, second + 1):
    if i % 7 == 0:
        print("all numbers divisible by 7 in range:", i, end=" ")
counter = 0
for i in range(first, second + 1):
    if i %5==0:
        counter +=1
print("all numbers divisible by 5 in range:",counter, end=" ")
        
        