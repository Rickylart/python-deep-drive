print("Welcome to tip calculator")

totalBill = float(input("What was the total bill ?\n$"))
totalPayers = int(input("How many people to split the bill ?\n"))
percentage = int(input("What percentage tip would you like to give ? 10, 12, or 15 ?\n"))

# calculate the tip percentage
tipAmount = totalBill * percentage / 100

# calculate the total amount
totalAmount = totalBill + tipAmount

# amount each person will pay
amountPerPerson = totalAmount / totalPayers

print("Each person should pay : " + str(amountPerPerson))
