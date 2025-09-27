def fun2():
    print("fun2 execution start")
    try:
        num=int(input())
        den=int(input())
        ans=num/den
        print(ans)
    except ZeroDivisionError:
        print("Catch in fun2")
    print("fun2 execution stop")
def fun1():
    print("fun1 execution start")
    try:
        fun2()
    except ZeroDivisionError:
        print("Catch in fun1")
    print("fun1 execution stop")

def main():
    print("main execution start")
    try:
        fun1()
    except ZeroDivisionError:
        print("Catch in main")
    print("main execution stop")    


try:
    main()
except ZeroDivisionError:
        print("Catch in main calling")