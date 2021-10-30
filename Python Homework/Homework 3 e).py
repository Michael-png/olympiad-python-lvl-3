print("Give me a three digit number and I will give you the sum of it's digits")
ThreeDigitNumber = int(input("Enter the three digit number: "))
OnesDigit = ThreeDigitNumber % 10
TensDigit = (ThreeDigitNumber % 100 - OnesDigit)/10
HundredsDigit = (ThreeDigitNumber - TensDigit * 10 - OnesDigit )/100
DigitsSum = OnesDigit + TensDigit + HundredsDigit
print(DigitsSum)
