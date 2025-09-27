print("MARK SHEET")
name=input("Enter Student Name : ")
rollno=int(input("Enter Roll No : "))   
dept=input("Enter Department : ")
m=[]
s=[]
t=0
av=0
g=""
while(True):
    sub=input("Enter subject name : ")
    mark=int(input("Enter marks :"))
    m.append(mark)
    s.append(sub)
    ch=input("Do you want to add more subject (y/n) : ")
    if ch.lower()!='y':
        break

for i in m:
    t=t+i

av=t/len(m)

if(av>=90):
    g="O"
elif(av>=80):
    g="A+"
elif(av>=70):
    g="A"   
elif(av>=60):
    g="B+"
elif(av>=50):
    g="B"
else:
    g="F"
print()
print("Student Name : ",name)   
print("Roll No : ",rollno)
print("Department : ",dept)
print()
print("Subject\t\tMarks")
for i in range(len(m)):
    print(s[i],"\t\t",m[i])
print()
print("Total Marks : ",t)
print("Average Marks : ",av)
print("Grade : ",g)