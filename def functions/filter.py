def eoro(l):
        if l%2==0:
            return True
        else:
            return False

l=[1,2,3,4,5]
f=list(filter(eoro,l))
print(f)