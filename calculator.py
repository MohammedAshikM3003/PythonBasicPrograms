while(True):
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        a=int(input("Enter 'A' value : "))
        b=int(input("Enter 'B' value : "))
        print(a ,'+', b,'=',a+b)
    elif(ch==2):
        a=int(input("Enter 'A' value : "))
        b=int(input("Enter 'B' value : "))
        print(a ,'-', b,'=',a-b)
    elif(ch==3):
        a=int(input("Enter 'A' value : "))
        b=int(input("Enter 'B' value : "))
        print(a ,'*', b,'=',a*b)
    elif(ch==4):
        a=int(input("Enter 'A' value : "))
        b=int(input("Enter 'B' value : "))
        print(a ,'/', b,'=',a/b)
    else:
        break

    