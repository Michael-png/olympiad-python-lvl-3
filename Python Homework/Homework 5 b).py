g = int(input("What is your age?"))
if 0 <= g < 18:
    print("You are to young to enter.")
elif g < 0:
    print("Invalid Input")
else:
    print("You are old enough to enter.")