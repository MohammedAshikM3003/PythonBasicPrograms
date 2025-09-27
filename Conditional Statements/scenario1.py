a=int(input("Enter your age : "))
m=int(input("Enter mark : "))
at=int(input("Enter Attendance percentage : "))
p=int(input("How many projects you have : "))
sp=int(input("Enter special number : "))
bp=0
if a>=18:
    print("Student is Eligible")
    if m>=85:
        if at>=80:
            if p>=5:
                for i in range(5,p+1):
                    bp=bp+1
                if m+at>170 and p+bp>50:
                    print("Mega Scholarship")
                else:
                    print("Not eligible for Mega Scholarship")
            else:
                print("Projet is less than 5")
        else:
            print("Attendance is less than 80%")
    else:
        print("Marks is less than 85")
else:
    print("Student is not Eligible")

if sp%2==0 and sp%3==0 :
    if sp//6==7 and sp%7!=0:
        print(sp,"is choosen")
    else:
        print(sp,"is not choosen")
else:
    print(sp,"is not choosen")