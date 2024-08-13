import random

easy_words = ["apple", "chair", "house", "river", "banana", "guitar", "pencil", "mountain",
    "orange", "computer", "sun", "tree", "cat", "dog", "car", "book", 
    "pizza", "shoe", "door", "ball", "phone", "fish", "star", "broom"]

hard_words = ["quartz", "xylophone", "zephyr", "awkward", "mnemonic", "crypt", "pneumonia", 
    "syndrome", "fuchsia", "juxtapose", "vortex", "phlegm", "sphinx", "rendezvous", 
    "buffoon", "gazebo", "whimsical", "quizzical", "subtle", "liaison", "bizarre", 
    "eccentric", "mischievous", "yacht", "rhythm"]

hangman = [["+---+"], 
           ["    |"], 
           ["    |"], 
           ["    |"], 
           ["   ==="]]


def displayIntro():
    print("\tWelcome to...\t")
    print("\tH A N G M A N\t")
    print()
   

def printHangman():
    for i in range(0, len(hangman)):
        print(hangman[i][0])



displayIntro()

gameIsRunning = True
while gameIsRunning == True:
    word = random.choice(easy_words) # Select a word
    userGuess = ["_" for i in range(0, len(word))]
    print(userGuess)
    printHangman()
    # askUser() # Show drawing and blanks to the player


