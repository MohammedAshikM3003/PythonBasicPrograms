t=(1,2,3,4)
print(len(t))
print(min(t))
print(max(t))
print(sorted(t))

#special function
a={10,20,30,40,50}
b={22,33,44}
print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))


z=frozenset((1,2,3))
print(type(z))
print(z)



'''
set

A set is a collection of unique elements.

Built-in data type in Python.

Unordered, unindexed, and does not allow duplicates.



s = {1, 2, 3, 3, 2}
print(s)


s = set([1, 2, 2, 3])
print(s)


s=set()
print(type(s))


s={}
print(type(s))


# Empty set
s = set()


s = set([1, 2, 2, 3])
print(s)


s = {10, 20, 30}
for item in s:
    print(item)



s={1,2,3,4,5,6,7,8}
s.add(100)
print(s)
s.update([4,5])
print(s)

# s.remove(101)
print(s)
s.discard(101)
s.pop()
s.clear()
print(s)


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # union 
print(a & b)
print(b - a)
print(a ^ b)

s = {1, 2, 3}
print(len(s))        
print(max(s))     
print(min(s))       
print(sum(s))

s1 = {1, 2,4,5,6,3}
s2 = {1,2}
print(s2.issubset(s1))
print(s2.issuperset(s1))
print(s1.isdisjoint(s2)) 

s=frozenset([1,2,3])
print(s)
s.add(100)
print(s)
'''