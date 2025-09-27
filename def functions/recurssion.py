def s(lst):
    if not lst:
        return 0
    return lst[0] + s(lst[1:])

l = [1, 2, 3, 4, 5]
ans = s(l)
print(ans)