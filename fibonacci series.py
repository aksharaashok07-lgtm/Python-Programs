n=int(input("Enter how many terms do you want in the fibonacci series"))
a=0
b=1

for i in range(n):
    c=a+b
    print(a, end=' ')
    a=b
    b=c
