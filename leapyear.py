ln=1000
if(ln%4==0 and ln%100!=0)or(ln%400==0):
    print(ln,"is a leap year")
else:
    print(ln,"is not a leap year")