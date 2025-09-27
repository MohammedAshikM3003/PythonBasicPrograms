'''def validate(mob):
    if len(mob)==10:
        print("valid")

    else:
        raise Exception("Invalid Mobile Number") 

mob=input("Enter mobile number : ")
validate(mob)'''



try:
    raise ZeroDivisionError("Denominator is Zero")

except ZeroDivisionError as e:
    print(e)