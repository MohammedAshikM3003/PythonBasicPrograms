n=input("Enter your name : ")
m=int(input("Enter your marks : "))
print()
print(n)
print(m)
print()
if(m>=90 and m<=100):
    print("YOUR EXCELLENCE!!!")
    print("Grade O")
elif(m>=80 and m<90):
    print("GREAT ACHIEVEMENT!!!")
    print("Grade A")
elif(m>=70 and m<80):
    print("WELL DONE!!!")
    print("Grade B")
elif(m>=60 and m<70):
    print("GOOD WORK!!!")
    print("Grade C")
elif(m>=50 and m<60):
    print("PASSED!!!")
    print("Grade D")
else:
    print("TRY AGAIN!!!")
    print("Grade F")