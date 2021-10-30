number = int(input("Enter your score"))
if 100 >= number >= 90:
    print("Your grade is a A!")
elif 80 < number < 90:
    print("Your grade is a B!")
elif 70 < number < 80:
    print("Your grade is C!")
elif 60 < number < 70:
    print("Your grade is D!")
elif 0 <= number < 60:
    print("Your grade is F")
