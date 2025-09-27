s=input()
c=""
#for i in range(-1,~(len(s)),-1):
#   print(s[i],end='')
for i in s:
    c=i+c
if c==s:
    print(c,"Palindrome")
else:
    print(c,"Not a Palindrome")