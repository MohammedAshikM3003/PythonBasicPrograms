'''eoro=lambda l: True if l%2==0 else False

l=[1,2,3]
ans=list(filter(eoro,l))
print(ans)'''


print(list(filter(lambda l: l%2==0,[1,2,3])))