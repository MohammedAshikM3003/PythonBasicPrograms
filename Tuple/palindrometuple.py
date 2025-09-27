t=eval(input("Enter a Tuple : "))
print(t,'palindrome') if t==t[::-1] else print(t,'Not palindrome')
print(sorted(t))