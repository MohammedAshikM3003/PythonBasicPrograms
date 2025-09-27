s='apple'
r=''
for i in s:
    if i in 'aeiouAEIOU':
        s=s.replace(i,'*')
        r=r+'*'
        
print(s)
