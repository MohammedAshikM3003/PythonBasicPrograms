m=int(input("Enter mark :"))
if m>=90 and m<=100:
    print("Grade O")
elif m>=80 and m<90:
    print("Grade A")
elif m>=70 and m<80:
    print("Grade B")
elif m>=60 and m<70:
    print("Grade C")
elif m>100:
    print("Invalid mark")
else:
    print("Fail")