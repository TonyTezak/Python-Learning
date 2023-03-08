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
import random

youEnter = input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors. ")
youChoose = int(youEnter)
computerChooses = random.randint(0,2)

if youChoose == 0:
  print(rock)
elif youChoose == 1:
  print(paper)
elif youChoose == 2:
  print(scissors)

print("The Computer Chooses:")

if computerChooses == 0:
  print(rock)
elif computerChooses == 1:
  print(paper)
elif computerChooses == 2:
  print(scissors)

if youChoose == computerChooses:
  print("It's a tie")
elif youChoose == 2 and computerChooses == 0:
  print("Computer wins")
elif youChoose == 0 and computerChooses == 2:
  print("You win")
else:
  if computerChooses > youChoose:
    print("Computer wins")
  elif youChoose > computerChooses:
    print("You win")