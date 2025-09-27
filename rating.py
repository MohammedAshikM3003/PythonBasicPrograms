rating=float(input("Enter the movie rating (out of 10):"))
if rating>=9:
    print("Rank 1 - Blockbuster Hit")
elif rating>=7.5 and rating<9:
    print("Rank 2 - SuperHit")
elif rating>=6 and rating<7.5:
    print("Rank 3 - Hit")
elif rating>=4 and rating<6:
    print("Rank 4 - Average")
else:
    print("Rank 5 - Flop")