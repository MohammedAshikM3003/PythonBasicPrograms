f=open('D:\\Python\\File Handling\\files\\r+.txt','r+')
f.write("This is r+ mode")
f.seek(0)
w=f.read()

print(w)
