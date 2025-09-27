'''def div(a,b):
    try:
        if b==0:
            raise ZeroDivisionError("Denominator cannot be zero")
        c=a/b
        print("Division is : ",c)
    except ValueError as ve:
        print("Value Error Occurred:", ve)
    except ZeroDivisionError as e:
        print(e)
    else:
        print("No Exception Occurred")
    finally:
        print("Execution Completed")

def main():
    a=int(input("Enter A number : "))
    b=int(input("Enter B number : "))
    div(a,b)
    

main()'''


'''try:
    raise ZeroDivisionError("Denominator cannot be zero")
    print('try block')
except ZeroDivisionError as e:
    print('except block',e)
finally:
    a=int(input("Enter your age : "))
    print(a)'''


b=0
raise ZeroDivisionError

print("Done")