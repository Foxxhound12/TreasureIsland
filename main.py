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
choice1=input("There are two paths ahead of you!\nDo you want to go \"left\" or \"right\" ?\n").lower()
if choice1 == "left":
    choice2=input("You are coming to a lake. There is a bridge that lets you cross it.\nDo you want to use the \"bridge\" or \"swim\" over to the other side ?(\n").lower() #lower function dazu um Eingabe an den string im if Statement anzugleiche. #
    # Sprich egal ob der Benutzer LEFT, Left, left oder andere Variationen davon eingibt, es kommt dabei immer "left" heraus!.
    if choice2 == "bridge":
        choice3=input("You are coming to a hut. You enter it and now you stand in a pathway consisting of 3 colored doors.\nWhich door do you choose ?The \"red\", \"yellow\" or \"blue\" one?\n").lower()
        if choice3 == "yellow":
            print("Congratulations! You have found the treasure!!!")
        elif choice3 == "red":
            print("You are burned to death by a lingering fire! Game over!!!")
        elif choice3 == "blue":
            print("You get eaten by a giant beast! Game over!!!")
        else:
            print("You have a heart attack and you die! Game over!!!")
    else:
        print("You are attacked by Piranhas and you bleed to death! Game over!!!")
else:
    print("You fall into a deep hole and die after you crushed your skull! Game over!!!")


