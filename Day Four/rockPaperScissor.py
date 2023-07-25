# This is a rock and scissors game, mini project/application
import random

print("Welcome to the rock and scissors game, please follow the instructions below \n")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

userChoose = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
cpuChoose = random.randint(0, 2)

gameImages = [rock, paper, scissors]

if userChoose == cpuChoose:
    print(f"You Chose {gameImages[userChoose]}\n CPU chose {gameImages[cpuChoose]}\n : Draw")
elif userChoose == 0 and cpuChoose == 1:
    print(f"You Chose {gameImages[userChoose]}\n CPU chose {gameImages[cpuChoose]}\n : You Win!")
elif userChoose == 0 and cpuChoose == 2:
    print(f"You Chose {gameImages[userChoose]}\n CPU chose {gameImages[cpuChoose]}\n :  You Win!")
elif userChoose == 1 and cpuChoose == 0:
    print(f"You Chose {gameImages[userChoose]}\n CPU chose {gameImages[cpuChoose]}\n :  You Lose!")
elif userChoose == 1 and cpuChoose == 2:
    print(f"You Chose {gameImages[userChoose]}\n CPU chose {gameImages[cpuChoose]}\n :  You Lose!")
elif userChoose == 2 and cpuChoose == 0:
    print(f"You Chose {gameImages[userChoose]}\n CPU chose {gameImages[cpuChoose]}\n :  You Lose!")
elif userChoose == 2 and cpuChoose == 1:
    print(f"You Chose {gameImages[userChoose]}\n CPU chose {gameImages[cpuChoose]}\n :  You Win!")
else:
    print(f"You Chose : {userChoose}\n CPU chose {gameImages[cpuChoose]}\n: You entered a wrong input so you lose !")
