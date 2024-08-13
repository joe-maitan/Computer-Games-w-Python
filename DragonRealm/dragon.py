import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share their treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight.''')

    print()
    

def chooseACave():
    validInput = False
    while validInput == False:
        print(f"Which cave will you go into? (1 or 2)")
        userInput = int(input())

        if userInput == 1 or userInput == 2:
            return userInput
        else:
            print("Try again.")


def checkCave(userChoice):
    print(f"You approach the cave...")
    time.sleep(2)

    print(f"It is dark and spooky...")
    time.sleep(2)

    print(f"A large dragon jumps out from in front of you! It opens their jaws and ...")
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if userChoice == friendlyCave:
        print(f"Gives you their treasure!")
    else:
        print(f"Swallows you whole!")


def tryAgain():
    validInput = False
    while validInput == False:
        print("Do you want to play again? (y or n)") 
        userIn = input().lower()

        if userIn == 'y':
            return True
        elif userIn == 'n':
            return False
        else:
            print("Invalid choice. Try again.")


gameIsRunning = True
while gameIsRunning:
    displayIntro()
    checkCave(chooseACave()) # Player chooses a cave -> Check for friendly or enemy dragon

    if tryAgain() == False: # Ask to play again
        break 