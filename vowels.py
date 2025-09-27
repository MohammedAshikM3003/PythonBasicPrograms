w=input("Enter a word : ")
v='aeiouAEIOU'
a=0
e=0
i=0
o=0
u=0
c=0
for f in w:
    if f in v:
        c+=1
        if f=='a' or f=='A':
            a=a+1
        elif f=='e' or f=='E':
            e=e+1
        elif f=='i' or f=='I':
            i=i+1
        elif f=='o' or f=='O':
            o=o+1
        elif f=='u' or f=='U':
            u=u+1
if c>0:
    if 0<a:
        print("Number of a's : ",a)
    if 0<e:
        print("Number of e's : ",e)         
    if 0<i:
        print("Number of i's : ",i)
    if 0<o:
        print("Number of o's : ",o)
    if 0<u:
        print("Number of u's : ",u)
    print("Total number of vowels :",c)
else:
    print("No vowels found")