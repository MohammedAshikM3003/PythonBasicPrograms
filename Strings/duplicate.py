s=input()
print(list(set(s)))
co=0
se=''
for i in set(s):
    co=s.count(i)
    if co>1:
        print(i)
l=list(set(se))
for i in l:
    print(i,end=' ')    

    
