'''s=input("Enter a Sentence : ")
l=s.split()
max=l[0]
for i in l:
    if len(max)<len(i):
       max=i
print(l)
print(max)
'''
t=input()
k=t.split()
s=max(k,key=len)
print(s)



