'''s1='hello'
s2='world'
print(s1,s2)
print(id(s1),id(s2))
print(s1[2],s1[3],s2[3])
print(id(s1[2]),id(s1[3]),id(s1[3]),id(s2[3]))
print(s1[4],s2[1])
print(id(s1[4]),id(s2[1]))
id=len(str(id(s1)))
print(id)
'''

s1=input("enter :")
s2=input("enter :")
print(id(s1))
print(id(s2))
if(s1 is s2):
    print("same")
else:
    print("Not same")




      