l=[10,2,30]
ma=l[0]
mi=l[0]
for i in l:
    if ma<i:
        ma=i
    else:
        mi=i
    
print(ma+mi)


s=sorted(l)
print(s[0]+s[-1])

print(max(l)+min(l))

l.sort()
print(l)