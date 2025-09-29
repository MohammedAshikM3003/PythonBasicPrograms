def choco(l):
    z = []
    Nz = []
    for item in l:
        if item == 0:
            z.append(item)
        else:
            Nz.append(item)
    return z, Nz


n = int(input())
l = list(map(int, input().split()))
z, Nz = choco(l)
r=Nz+z
rs=' '.join(map(str,r))
print(rs)


