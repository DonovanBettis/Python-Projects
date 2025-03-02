Cup_Price = 0.75
Mug_Price = 1.5
Cookie_Price = 0.65

Cups = int(input("Enter number of cups of hot chocolate: "))
Mugs = int(input("Enter number of mugs of hot chocolate: "))
Cookies = int(input("Enter number of cookies: "))

Cups_Total = float(Cups*Cup_Price)
Mugs_Total = float(Mugs*Mug_Price)
Cookies_Total = float(Cookies*Cookie_Price)

Total = (Cups_Total + Mugs_Total + Cookies_Total)

print("Amount Due = $%.2f" % Total)

MoneyPaid = float(input("Enter the amount of money paid: "))

while MoneyPaid < Total:
    print("Insufficient funds. Please attempt payment again")
    MoneyPaid = float(input("Enter the amount of money paid: "))

Change = MoneyPaid - Total

print("***************************************")

print("Donovan's Hot Chocolate Stand Bill\n")

print("Cups of Hot Chocolate")
print("Number = " + str(Cups) + "        Cost = $%.2f" % Cups_Total)

print("Mugs of Hot Chocolate")
print("Number = " + str(Mugs) + "        Cost = $%.2f" % Mugs_Total)

print("Cookies")
print("Number = " + str(Cookies) + "        Cost = $%.2f" % Cookies_Total + "\n")

print("Total                  = $%.2f" % Total)
print("Money Paid             = $%.2f" % MoneyPaid)
print("Change Due             = $%.2f" % Change + "\n")


print("Thanks - Have a Great Day - Come Again!")


print("***************************************")
