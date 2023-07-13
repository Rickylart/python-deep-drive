print("Welcome to the RickyRich Pizza Joint")

size = input("What size pizza do you want ? S, M, L : ")
add_pepperoni = input("Do you want pepperoni ? Y or N : ")
extra_cheese = input("Do you want extra Cheese ? Y or N : ")
bill = 0

if size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is ${bill}")
        else:
            print(f"Your final bill is ${bill}")
    elif extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is ${bill}")
        else:
            print(f"Your final bill is ${bill}")
    elif extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")
elif size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is ${bill}")
        else:
            print(f"Your final bill is ${bill}")
    elif extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")
else:
    print("Please enter a valid size: eg - L, M, S")
