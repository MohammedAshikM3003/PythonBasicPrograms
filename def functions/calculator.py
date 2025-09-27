def add():
    a=int(input("\nEnter 'A' value : "))
    b=int(input("Enter 'B' value : "))
    print(f"{a} + {b} =",a+b)

def sub():
    a=int(input("\nEnter 'A' value : "))
    b=int(input("Enter 'B' value : "))
    print(f"{a} - {b} =",a-b)

def mul():
    a=int(input("\nEnter 'A' value : "))
    b=int(input("Enter 'B' value : "))
    print(f"{a} X {b} =",a*b)

def div():
    a=int(input("\nEnter 'A' value : "))
    b=int(input("Enter 'B' value : "))
    print(f"{a} / {b} =",a/b)

def rem():
    a=int(input("\nEnter 'A' value : "))
    b=int(input("Enter 'B' value : "))
    print(f"{a} % {b} =",a%b)


print('-'*40)
print("\t\tCALCULATOR")
print('-'*40)
while True:
    print("\n1.Addition\n2.Subraction\n3.Multiplication\n4.Divison\n5.Remainder")
    ch=int(input("\nEnter Your choice Number : "))
    if ch == 1:
        add()
        c=input("\nDo you want to continue ? <Yes/No> ")
        if c in ['No','no','n','N']:
            print('_'*40)
            break
    elif ch == 2:
        sub()
        c=input("\nDo you want to continue ? <Yes/No> ")
        if c in ['No','no','n','N']:
            print('_'*40)
            break
    elif ch == 3:
        mul()
        c=input("\nDo you want to continue ? <Yes/No> ")
        if c in ['No','no','n','N']:
            print('_'*40)
            break
    elif ch==4:
        div()
        c=input("\nDo you want to continue ? <Yes/No> ")
        if c in ['No','no','n','N']:
            print('_'*40)
            break
    elif ch==5:
        rem()
        c=input("\nDo you want to continue ? <Yes/No> ")
        if c in ['No','no','n','N']:
            print('_'*40)
            break
    else:
        print("\nInvalid choice !!!")