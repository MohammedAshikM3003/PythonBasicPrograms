#swapping of two numbers without using third variable
a=int(input("Enter 'A' value :"))
b=int(input("Enter 'B' value :"))
a=a+b
b=a-b
a=a-b
print("A value is : ",a)
print("B value is : ",b)

#swapping with third variable
x=int(input("Enter 'A' value :")) 
y=int(input("Enter 'B' value :"))
temp=0
temp=x
x=y
y=temp
print("A value is : ",x)
print("B value is : ",y)
