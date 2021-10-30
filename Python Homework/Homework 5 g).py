print("If you give me a number, I can tell you if it is odd or even.")
OddEven = int(input("Enter the number here: "))
if OddEven % 2 == 0:
    print("The number you have given me is even.")
elif OddEven % 2 == 1:
    print("The number you have given me is odd.")
elif OddEven <= 0:
    print("The number cannot be negative or zero")
else:
    print("Invalid Input")