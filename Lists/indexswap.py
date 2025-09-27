n=[0,1,2,3,4,5]
a=[]
for i in range(len(n)):
    if i%2!=0:
        a.insert(0,n[i])
    else:
        a.insert(1,n[i])
    
print(a)
