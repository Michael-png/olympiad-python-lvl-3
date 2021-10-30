# if you're supposed to count the number of positive numbers, the prompt doesn't say that.
print("If you enter six numbers, I will add up all the negative numbers and tell you how many negative numbers there are. ")
One = 0
Zero = 0
x = 0
while x > 6: #this while loop looks like it never runs
    x = x + 1
    InputSomething = int(input("Enter a number: "))
    if InputSomething < 0:
        Zero = Zero + InputSomething
    if InputSomething > 0:
        One = One + 1
print(Zero)
print(One)