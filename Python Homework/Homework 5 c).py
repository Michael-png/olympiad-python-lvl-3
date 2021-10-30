print("Input two numbers and I will give you the quotient result between the first and second number you input.")
FirstNumber = int(input("Enter the first number"))
SecondNumber = int(input("Enter the second number"))
ThirdNumber = FirstNumber/SecondNumber
if SecondNumber == 0:
    print("Dividing by zero is undefined.")
else:
    print("The quotient of the first and second number is " + str(ThirdNumber))
