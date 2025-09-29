l=[1,2,4,5,7]
for i in range(len(l)-1):
    if l[i+1]-l[i]>1:
        print("Missing:",l[i]+1)