import random
n=random.randint(1,20)

print("Welcome to number guessing game")

for i in range (5):
    a=int((input("Guess a number between 1 to 20 :")))
    if(a>n):
        print(f"{a} is too high")
    elif(a<n):
        print(f"{a} is too low")
    else:
        break

if(a==n):
    print(f"Congratulations! You guessed the number {n} correctly")
else:
    print(f"Sorry! The number is {n}. Better luck next time")