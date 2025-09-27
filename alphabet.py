w=input("Enter 'lower/UPPER' :")
if w=='lower':
    for i in range(97, 123):
        print(chr(i),end=' ')
else:
    for i in range(65,91):
        print(chr(i),end=' ')
