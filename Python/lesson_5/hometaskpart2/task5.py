expression=input("Введіть математичний вираз (наприклад, 3+5): ")
a,b=expression.split('+') if '+' in expression else \
     expression.split('-') if '-' in expression else \
     expression.split('*') if '*' in expression else \
     expression.split('/')
a=float(a)
b=float(b)
result=a+b if '+' in expression else \
       a-b if '-' in expression else \
       a*b if '*' in expression else \
       a/b
print(result)
