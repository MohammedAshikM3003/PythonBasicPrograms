s=input("Enter a String : ")
c=0
v=0
for i in s:
    if i.isalpha():
        if i in 'aeiouAEIOU':
            v=v+1
        else:
            c=c+1
print('Vowels count : ',v)
print('Constant count :',c)

for i in range(len(s)-2):
    print(s[i:i+3])

