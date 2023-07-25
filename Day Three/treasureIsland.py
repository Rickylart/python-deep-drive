print("***********************************************************************\n"
      "Welcome to the Treasure Island.\nYour mission is to find the treasure\n"
      "***********************************************************************")
direction = input("Which way do you want to pass ? left or right \n").lower()

if direction == 'left':
    activity = input("Do you want to wait for the boat or swim across ? swim or wait \n").lower()
    if activity == 'wait':
        door = input("Which door color , do you prefer ? red or blue or yellow \n").lower()
        if door == 'red':
            print("Burned by fire.\n Game Over")
        elif door == 'blue':
            print("Eaten by beasts.\n Game Over")
        elif door == 'yellow':
            print("You Win!.\n Congrats")
        else:
            print("Game Over, you beans!!!")
    else:
        print("Attacked by trout.\n Game Over")
else:
    print("Fell into a hole.\n Game Over")


