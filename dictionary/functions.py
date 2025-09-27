d={'A':100,'B':200}
e='B'
#d.pop('A')
#del d
print(d)
print(e in d)




'''
student = dict(name="Alice", age=20, course="Python")

print(student)



d = {"a": 1, "b": 2, "a": 3}
print(d)


person = {"name": "John", "age": 25}

person["city"] ="New York"

print(person)

person["age"]=20


#person.pop("age") 
#person.popitem() 
#print(person)
print(person)
del person["city"]
print(person)
person.clear()
print(person)




d1 = {"a": 1, "b": 2}
d2 = {"c": 3}

d3 = d1 | d2
print(d3)

print("a" in d1)
print("z" not in d1)


d = {"a": 1, "b": 2, "c": 3}
print(d.keys())
print(d.values())
print(d.items())
print(d.get("a"))
print(d.setdefault("d", 0))
print(d)
d.update({"b": 5, "e": 6})
print(d)
d2 = d.copy()
print(d2)

'''
student = {"name": "Alice", "age": 21, "marks": 90}

for values in student.items():
    print(values)
