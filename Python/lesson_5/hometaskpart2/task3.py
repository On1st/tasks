import random
numbers=[random.randint(-10,10) for _ in range(20)]
min_positive=min((x for x in numbers if x>0),)
max_negative=max((x for x in numbers if x<0),)
count_negative=sum(1 for x in numbers if x<0)
count_positive=sum(1 for x in numbers if x>0)
count_zeros=numbers.count(0)
print("Список:", numbers)
print("Мінімальний додатний елемент:", min_positive)
print("Максимальний від'ємний елемент:", max_negative)
print("Кількість від'ємних чисел:", count_negative)
print("Кількість додатних чисел:", count_positive)
print("Кількість нулів:", count_zeros)
