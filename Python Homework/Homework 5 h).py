print("If you give me the mass of two objects in kilograms and grams, I can give you the total mass the two objects make up.")
KilogramsOne = int(input("Enter the kilograms of the first object : "))
GramsOne = int(input("Enter the grams of the first object(The mass in grams can be zero if it is not a decimal) : "))
KilogramsTwo = int(input("Enter the kilograms of the second object : "))
GramsTwo = int(input("Enter the grams of the second object(The mass in grams can be zero if it is not a decimal) : "))
TotalMass = ((KilogramsOne + KilogramsTwo) * 1000 + GramsOne + GramsTwo)/1000
KilogramsTotal = KilogramsOne + KilogramsTwo
GramsTotal = GramsOne + GramsTwo
TotalMassTwo = str(str(KilogramsTotal) + " kg " + str(GramsTotal) + " grams.")
if KilogramsOne <= 0:
    print("Mass cannot be negative or zero")
elif GramsOne <= 0:
    print("Mass cannot be negative or zero")
elif KilogramsTwo <= 0:
    print("Mass cannot be negative or zero")
elif GramsTwo <= 0:
    print("Mass cannot be negative or zero")
print("The total mass of the two objects in kilograms is " + str(TotalMass) + " or " + str(TotalMassTwo))

