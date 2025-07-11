nums=[int(x) for x in input("Введіть числа через пробіл: ").split()]
positives=sorted([x for x in nums if x>=0])
i=0
result=[]
for x in nums:
    if x<0:
        result.append(x)
    else:
        result.append(positives[i])
        i+=1
print(*result)
