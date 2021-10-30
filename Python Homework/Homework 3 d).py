print("If you tell me a conglomerate of coins, I can tell you how much money you have in total")
Nickel = int(input("Enter the Nickels in here: "))
Dime = int(input("Enter the dimes in here "))
Quarter = int(input("Enter the quarters in here: "))
Loonie = int(input("Enter the loonies in here: "))
Toonie = int(input("Enter the toonies in here: "))
TotalAmountOfMoney = Nickel * 0.05 + Dime * 0.1 + Quarter * 0.25 + Loonie * 1 + Toonie * 2
TotalAmountOfMoneyContinued = TotalAmountOfMoney * 100
print("The total amount of money you have %.2f" % (TotalAmountOfMoney))
