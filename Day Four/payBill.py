import random

print("Who will buy the meal")

names = input("Give me everybody's names, seperated by comma : ")
getNames = names.split(",")

pickWhoWillPay = random.randint(0, len(getNames) - 1)
whoWillPay = getNames[pickWhoWillPay]

print(f"{random.choice(getNames)} is paying for the meal today.")
print(whoWillPay+" is paying for the meal today.")
