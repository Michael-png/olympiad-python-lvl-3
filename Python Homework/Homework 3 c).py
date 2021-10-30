print("Give me two numbers and I will give you the quotient of the dividend to the divisor in the decimal and remainder form.")
Dividend = int(input("Enter the dividend: "))
Divisor = int(input("Enter the divisor: "))
DecimalResult = Dividend / Divisor
RemainderResult = Dividend % Divisor
RemainderResultContinued = Dividend // Divisor
print("The quotient of %s to %s is %s or %s remainder %s." % (Dividend, Divisor, DecimalResult, RemainderResultContinued, RemainderResult))