M=[1,2,3,4,1,2,3,1]  
M.sort()
N=set()
for i in range(len(M)-1):
        if M[i] == M[i+1]:
            N.add(M[i])
            print(M[i])
print(N)

