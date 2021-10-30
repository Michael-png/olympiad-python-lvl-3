print("If you input your three test score percentages, I can tell you if you pass or fail")
TestPercentageOne = int(input("Enter your first test score: "))
TestPercentageTwo = int(input("Enter your second test score: "))
TestPercentageThree = int(input("Enter your third test score: "))
PassFail = (TestPercentageOne + TestPercentageTwo + TestPercentageThree)/3
if PassFail < 50:
    print("You Fail")
elif PassFail < 0:
    print("You cannot input a negative test score")
elif PassFail >= 100:
    print("You cannot have test scores above 100%")
elif PassFail >= 50:
    print("You Pass")
else:
    print("Invalid Input")