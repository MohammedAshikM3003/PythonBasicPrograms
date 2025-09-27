'''on=int(input("Enter a number : "))
dn=on
rv=0
while(on>0):
    t=on%10
    rv=(rv*10)+t
    on=on//10

if(dn==rv):
    print(f"{dn} is a palindorme")
else:
    print(f"{dn} is not a palindorme")
'''

'''n=input("Enter a value : ")
r=n[::-1]
if n==r:
    print(n,"is a palindorme")
else:
    print(n,"is not a palindorme")
'''

n=input
du=n
r=0
while du!=0:
    g=du%10
    r=(r*10)+g
    du=du//10
