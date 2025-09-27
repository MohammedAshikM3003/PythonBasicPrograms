'''p=int(input("Enter a number: "))
if p>1:
    for i in range(2,p):
        if(p%i)==0:
            print(p,"is not a prime number")
            break
    else:
        print(p,"is a prime number")
else:
    print(p,"is not a prime number")'''

n=int(input("Enter a number : "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")