'''
A tuple is a collection in Python.
Similar to a list, but immutable (cannot be changed after creation).
Ordered, indexed, and allows duplicates.
'''
t= (5,)
print(t)
print(type(t))


mixed = (1, "hello", 3.14, True)
print(mixed)


t = (10, 20, 30, 40,50,60)
print(t[0])
print(t[-1])


t = (10, 20, 30, 40,50,60)
print(t[::2])



t = (10, 20, 30, 40,50,60)
t[0]=5
print(t)



t = (10, 20, 30, 40,50,60)
lst = list(t)
lst[0]=100
lst[2]=300
lst[-1]=600

t=tuple(lst)
print(t)
print(10 not in t)



t=(1, 9, 2, 5 , 6 ,8, 2)
print(sorted(t))




t= 10, 20, 30, 40
print(t)

a,b,c,d =t
print( a,b,c,d)




nested = (1,(2,3),(4,5,6))
print(nested)
print(nested[1])


person = ("Alice", 25, ["Python", "Java"])
print(person)

person[2].append("c")
print(person)
