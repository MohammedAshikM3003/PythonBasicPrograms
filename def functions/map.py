from functools import reduce

def pow(x):
    return x**2

l=[1,2,3,4,5]
a=list(map(pow,l))
print(a)


def pow(x):
    return x**2

l=[1,2,3,4,5]
a=reduce(pow,l)
print(a)