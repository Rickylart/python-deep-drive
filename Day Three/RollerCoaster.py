print("Welcome to Roller Coaster Yaaaa!!!!")

height = int(input("Enter your height in cm ?"))
bill = 0

if height >= 120:
    age = int(input("Enter your age ? "))
    if age >= 18:
        bill = 20
        print(f"You can ride the roller coaster and the price is {bill}$")
    elif age > 12:
        bill = 15
        print(f"You can ride the roller coaster and the price is {bill}$")
    else:
        bill = 10
        print(f"You can ride the roller coaster and the price is {bill}$")

    takePicture = input("Will you like to take a picture ? Y for Yes and N for No : ")
    if takePicture == 'Y' or takePicture == 'Yes':
        bill += 3
    print(f"Total price is {bill}$")
else:
    print(f"Sorry you are not eligible to ride")
