print("Give me a number for the base and the exponent and I will give you the result")
Base = int(input("Enter the base here: "))
Exponent = int(input("Enter the exponent here: "))
Result = Base ** Exponent
print("The exponent of " + str(Base) + " to the " + str(Exponent) + " is " + str(Result))
print("The exponent of %d to the %d is %d" % (Base, Exponent, Result))