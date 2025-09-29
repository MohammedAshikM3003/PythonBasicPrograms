with open('D:\\Python\\File Handling\\files\\test.txt','r') as f:
    w=f.readlines()
    print(w)
    print(type(w))
    for i in w:
        print(i)


