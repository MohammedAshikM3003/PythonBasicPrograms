from functools import reduce
lst=[1,2,3,4,5]
def fun(x,y):
    return x+y

ans=reduce(fun,lst)
print(ans)