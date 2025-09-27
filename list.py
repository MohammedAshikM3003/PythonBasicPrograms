#Get input from user and store it into a List
l=[]
while(True):
    print("1.Adding new element\n2.Delete element\n3.Replace element\n4.Search element\n5.Dispaly\n6.Exit\n")
    ch=int(input("Enter Your choice : "))
    print()
    if(ch==1):
        a=int(input("Enter number : "))
        l.append(a)
        print(a,"is added to list")
        print()
    elif(ch==2):
        d=int(input("Deleting number : "))
        for i in l:
            if(d==i):
                l.remove(i)
        print(d,"is Deleted")
        print()
    elif(ch==3):
        r=int(input("Which number want to replace ? "))
        nr=int(input(f"{r} is replacing with ? "))
        f=0
        for i in l:
            if(r==i):
                index=l.index(r)
                l.pop(index)
                l.insert(index,nr)
                f=1 
        if(f!=0):
            print(r,"is replaced with",nr)
        else:
                print(r,"is not found retry")
        print()
    elif(ch==4):
        s=int(input("Enter value to Search : "))
        f=0
        for i in l:
            if(s==i):
                f=f+1
        if(f!=0):
            print(s,"is found on index",l.index(s))
        else:
            print(s,"is not found")
        print()
    elif(ch==5):
        print(l)
        print()
    elif(ch==6):
        break
    else:
        print("Invalid choice")
        print()
