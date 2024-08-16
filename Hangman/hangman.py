import random

LIST_OF_EASY_WORDS = ["apple", "chair", "house", "river", "banana", "guitar", "pencil", "mountain",
    "orange", "computer", "sun", "tree", "cat", "dog", "car", "book", 
    "pizza", "shoe", "door", "ball", "phone", "fish", "star", "broom"]

LIST_OF_HARD_WORDS = ["quartz", "xylophone", "zephyr", "awkward", "mnemonic", "crypt", "pneumonia", 
    "syndrome", "fuchsia", "juxtapose", "vortex", "phlegm", "sphinx", "rendezvous", 
    "buffoon", "gazebo", "whimsical", "quizzical", "subtle", "liaison", "bizarre", 
    "eccentric", "mischievous", "yacht", "rhythm"]

HANGMAN_BOARDS = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
O   |
    |
    |
   ===''', '''
+---+
O   |
|   |
    |
   ===''', '''
+---+
O   |
\/| |
    |
   ===''',
   '''
+---+
O   |
|\  |
    |
   ===''',
   '''
+---+
    |
    |
    |
   ===''',
   '''
+---+
    |
    |
    |
   ===''']


def displayIntro():
    print("\tWelcome to...\t")
    print("\tH A N G M A N\t")
    print()
   

def askUser(word):
    # Ask user for a letter in the word
    print(f"What is your guess?")
    guessLetter = input()

    return guessLetter


def validateGuess(word, char):
    if char in word:
        return True
    else:
        return False


def fillInBlank(userGuess, word, char):
    for i in range(0, len(word)):
        if word[i] == char:
            userGuess[i] = char


def fillInBoard():
    return None


def startGame():
    gameIsRunning = True
    numGuesses = 0 # max number of guesses can only be 6 because there are only 

    word = random.choice(LIST_OF_EASY_WORDS) # Select a word
    
    while gameIsRunning == True:
        userBoard = HANGMAN_BOARDS[numGuesses]
        
        userGuess = str(["_" for i in range(0, len(word))])
        print(userGuess)
        # printHangman(userBoard)

        tempChar = askUser(word)
        if validateGuess(word, tempChar) == True:
            fillInBlank(userGuess, word, tempChar) # Player got the guess right, fill in the correct blank
        else:
            # player got the guess wrong, add to the hangman board
            return

        

# displayIntro()
# while True:
# startGame()

for i in range(0, len(HANGMAN_BOARDS)):
    print(HANGMAN_BOARDS[i])
