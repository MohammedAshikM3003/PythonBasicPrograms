print("Execution Starts")
lst=[10,20,30,0,50,60]
di={1:"c",2:"c++",3:"python",4:"java"}
try:
    n=int(input("Enter a key : "))
    print(di[n])
    num=int(input())
    print(lst[num])
    den=int(input())
    print(lst[den])
    ans=lst[num]/lst[den]
    print(ans)

except ZeroDivisionError:
    print("Denominator cannot be zero !!!")

print("Execution Ends")