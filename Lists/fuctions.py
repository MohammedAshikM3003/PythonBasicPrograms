# Example: enter numbers like 10 20 30 40

'''
lst = list(map(int,input().split()))
print(lst)

lst = input().split()
print(lst)


n=int(input())
lst=[]

for i in range (n):
    val = input()
    lst.append(val)
print(lst)


lst =[10,20,30,40,50,60]
print(lst)
# lst = lst + [111,222,333]
lst.extend([111,22,333])
lst.insert(3,999)
lst[]=11111
print(lst)



num =[10,20,30,40,50,60,70,80]

max_val = num[0]
min_val = num[0]


for i in num:
    if i>max_val :
        max_val=i
    if i<min_val:
        min_val=i
        
print(max_val + min_val)




lst1 =[[1,2,3],[4,5,6]]
lst2 = list (lst1)
print(id(lst1))
print(id(lst2))
print(lst1)
print(lst2)
print(lst1 is lst2)
lst1.append([50,60])
print(lst1)
print(lst2)
lst1[1][0]=300
lst1[1][1]=999

print(lst1)
print(lst2)


'''




numbers = [3, 7, 2, 9, 5]
words = ["apple", "banana", "cherry"]
'''
print("max():", max(numbers))
print("min():", min(numbers))
print("len():", len(words))
print("range():", list(range(1, 6)))



print("any():", any([0, 1, 0]))
print("all():", all([1, 1, 1]))

print("sum():", sum(numbers))

print("enumerate():")
for i, w in enumerate(words):
    print(i, w)

print("eval():", eval("5 + 10 * 2"))
print("list():", list("hello"))
'''
print("sorted():", sorted(numbers))
print("reversed():", list(reversed(words)))





