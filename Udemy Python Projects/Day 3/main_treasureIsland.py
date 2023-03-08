print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("In front of you is a corn field. There are two paths.")
leftRight = input('Do you go "left" or "right"?\n')

if leftRight.lower() == "left":
  print("You come to a lake. There's an island in the middle of the lake.")
  swimWait = input('Do you "swim", or "wait" for a boat?\n')
  if swimWait.lower() == "wait":
    print("You reach an island. There is rock wall, where you see three doors.")
    whichDoor = input('Which door do you choose? "Red", "Yellow", or "Blue"?\n')
    if whichDoor.lower() == "red":
      print("Oh hey, you've found my large vat of strawberry preserves! Good luck getting out. Game over.")
    elif whichDoor.lower() == "blue":
      print("You've fallen into a alternate reality, where you infinitely fall up into the sky. Game over.")
    elif whichDoor.lower() == "yellow":
      print("Yellow doors lead to golden treasures. You win!")
      print("Um, I hope that boat can hold the weight of all of this gold...")
    else:
      print("The door you chose doesn't exist. Suddenly, neither do you.  Game over.")
  else:
    print("While swimming, you are hit by the boat you should have waited for. Game over.")
else:
  print("You get lost in the Corn Maze of Endless Mediocrity. Game over.")
