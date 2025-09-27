s=[10,20,999,40,50,999,60,70,999]
r=999
for i in s:
    if r in s:
        s.remove(r)
print(s)