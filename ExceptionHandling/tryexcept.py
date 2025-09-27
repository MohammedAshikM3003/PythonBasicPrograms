print("BANK ACCOUNT HAS BEEN CONNECTED")
try:
    p=int(input("Enter the principle amount : "))
    r=20
    t=int(input("Enter the time in years : "))
    si=(p*r*t)/100
    print("The simple interest is : ",si)

except:
    print("Please enter valid input")

else:
    si=(p*r*t)/100
    print("The simple interest is : ",si)

print("BANK ACCOUNT HAS BEEN CLOSED")