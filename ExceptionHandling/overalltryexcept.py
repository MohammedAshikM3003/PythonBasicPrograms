def list():
    l=[]
    n=int(input("Enter length of list : "))
    for i in range(0):
        try:
            n=int(input("Enter length of list : "))
            for i in range(n):
                ele=int(input("Enter element : "))
                l.append(ele)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    else:
        print("List =",l)
        print("Division operation range is from index of 0 to",n-1)
        try:
            num=int(input("Enter numerator index : "))
            den=int(input("Enter denominator index : "))
            ans=l[num]/l[den]
            print("Answer = ",ans)
        except IndexError:
            print("Index out of range. Please enter valid indices.")
        except ZeroDivisionError:
            print("Denominator cannot be zero. Please enter a non-zero denominator index.")


def dict():
    d={}
    while True:
        try:
            n=int(input("Enter number of key-value pairs : "))
            for i in range(n):
                key=int(input("Enter key : "))
                value=input("Enter value : ")
                d[key]=value
            print("Invalid input. Please enter an integer for the key.")

        except ValueError:
            print("Invalid input. Please enter an integer for the key.")
    else:
        di=input("Enter a key to access its value : ")
        try:
            print("Value =",d[di])
        except KeyError:
            print("Key not found.")
    print("Dictionary =",d)


print("Execution Starts")
print("1. List\n2. Dictionary")
ch=int(input("Enter your choice : "))
if ch==1:
    list()
elif ch==2:
    dict()
else:
    print("Invalid choice.")
