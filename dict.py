dict={'A':1,'B':2,'C':3,'A':4}
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get('A'))
print(dict.get('D','Not Found'))
for k,v in dict.items():
    print(k,":",v)

dict['D']=4
del dict['B']
print(dict)
print(len(dict))
print(dict.pop('C'))
print(dict)
dict.clear()
print(dict)