# Your program should allow you to enter the position of the treasure using two digit system.
# The first digit is the horizontal column number and the second digit is the vertical row number
# *****************************************************************************************************
storage1 = [" ", " ", " "]
storage2 = [" ", " ", " "]
storage3 = [" ", " ", " "]

island = [storage1, storage2, storage3]

print(f"{storage1}\n{storage2}\n{storage3}\n")

position = input("Where do you want to put the treasure ? ")
horizontal = int(position[0])
vertical = int(position[1])

island[vertical - 1][horizontal - 1] = 'x'

print(f"{storage1}\n{storage2}\n{storage3}")

