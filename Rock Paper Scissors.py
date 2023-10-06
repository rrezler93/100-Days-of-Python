# Rock, paper, scissors game

# Imports
import random

# Signs
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

#Write your code below this line 👇

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer = random.randint(0, 2)
winner = ""

if user == 0:
    print("\nYour chose:")
    print(rock)
    if computer == 0:
        winner = "draw"
    elif computer == 1:
        winner = "computer"
    else:
        winner = "user"
elif user == 1:
    print("\nYour chose:")
    print(paper)
    if computer == 0:
        winner = "user"
    elif computer == 1:
        winner = "draw"
    else:
        winner = "computer"
else:
    print("\nYour chose:")
    print(scissors)
    if computer == 0:
        winner = "computer"
    elif computer == 1:
        winner = "user"
    else:
        winner = "draw"

if computer == 0:
    print("\nComputer chose:")
    print(rock)
elif computer == 1:
    print("\nComputer chose:")
    print(paper)
else:
    print("\nComputer chose:")
    print(scissors)

if winner == "user":
    print("\nYou won!")
elif winner == "computer":
    print("\nYou lost!")
else:
    print("\nDraw!")

