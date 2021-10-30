print("Enter the hours of someone working to repair a device or more that you own, and the cost of the parts used after and I shall tell you the charge of your order.")
HoursWorked = int(input("Enter the work hours of the technician working for you"))
PartsCost = int(input("Enter the cost of the parts used to fix your device"))
FullCost = (HoursWorked * 100) + PartsCost
if FullCost < 150:
    print("The minimum cost for a technician is at least 150$")
else:
    print("The cost of the repair is " + str(FullCost))

