l=[]
t=[]
while(True):
    print('1.Add new Task\n2.Task Completed\n3.View Tasks\n4.Exit')
    ch=int(input("Enter your choice : "))
    if(ch==1):
        a=input("Enter new Task : ")
        l.append(a)
        b=input("Enter Time : ")
        t.append(b)
        print("Task added")
    elif(ch==2):
        c=input("Which Task Completed : ")
        for i in l:
            if(c==i):
                index=l.index(i)
                print(f"{c} {t[index]} task is completed")
                l.pop(index)
                t.pop(index)
            else:
                print(f"{c} task is not found")
    elif(ch==3):
        print("\nPending Tasks are")
        for i in range(0,len(l)):
            print(l[i],""*5,t[i]) 
        print()
    else:
        print("Invalid Choice")



