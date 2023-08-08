print("Welcome to the PyPassword Generator")
import random

letters = ['a','b','c','e','f','g','h','i','j','k','l','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','^','&','*','(',')','-','_','+','=']

numberOfLetters = int(input("How many letters would you like in your password?\n"))
numberOfSymbols = int(input("How many symbols would you like?\n"))
numberOfNumbers = int(input("How many numbers would you like?\n"))

password = ""
firstPass = ""
secondPass = ""
thirdPass = ""

# number of letters
for char in range(1, numberOfLetters + 1):
    randomChar = random.choice(letters)
    password += randomChar
    firstPass += randomChar

# number of symbols
for symbol in range(1, numberOfSymbols + 1):
    randomSym = random.choice(symbols)
    password += randomSym
    secondPass += randomSym

# number of numbers
for number in range(1, numberOfNumbers + 1):
    randomNum = random.choice(numbers)
    password += randomNum
    thirdPass += randomNum

# easy way
print(f"Easy way : {password}")

# hard way
passwordList = [firstPass,secondPass,thirdPass]
random.shuffle(passwordList)


strongPassword = ""
for strong in passwordList:
    strongPassword += strong

print(f"Hard way : {strongPassword}")

print(f"{numberOfLetters,numberOfSymbols,numberOfNumbers}")
