Number = 0
x = 0
while x > 6: #this while loop looks like it never runs
    x = x + 1
    SomeKindOfInput = int(input("Enter a number here: "))
    OddNumbers = SomeKindOfInput % 2
    if OddNumbers == 1:
        Number = Number + OddNumbers
    print(Number)
