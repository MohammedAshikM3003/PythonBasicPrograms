'''n=int(input("Enter a value : "))
if n>=0:
    if n%2==0:
        print(n,"is even")
    else:
        print(n,"is odd")
else:
    print(n,"is negative")
    if n%2==0:
        print(n,"is even")
    else:
        print(n,"is odd")
'''

'''a=int(input("Enter age :"))
if a>20:
    print("Teen")
    if a>=18:
        print("Eligible for voting")
    else:
        print("Not Eligible for voting")
else:
    print("Not Teen")
'''

a=int(input("Enter 'A' value : "))
b=int(input("Enter 'B' value : "))
c=int(input("Enter 'C' value : "))
if a>b:
    if a>c:
        print(a,"is greater")
elif b>a:
    if b>c:
        print(b,"is greater")
else:
    print(c,"is greater")