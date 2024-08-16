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
/|   |
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
 O   |
/|\  |
 /\  |
    ===''']


def displayIntro():
    print("\tWelcome to...\t")
    print("\tH A N G M A N\t")
    print()


def createWordBlanks(wordToGuess):
    temp = ""
    for i in range(0, len(wordToGuess)):
        if i + 1 == len(wordToGuess):
            temp += '_'
        else:
            temp += '_ '
    
    return temp
   

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


def fillInBlank(blankWordString):
    print(len(blankWordString))
    # for i in range(0, len(word)):
    #     if word[i] == char:
    #         blankWordString[i] = char


def startGame():
    gameIsRunning = True
    numGuesses = 0 # max number of guesses can only be 6 because there are only 

    wordToGuess = random.choice(LIST_OF_EASY_WORDS) # Select a word
    
    while gameIsRunning == True:
        userBoard = HANGMAN_BOARDS[numGuesses]
        wordBlanks = ['_' for i in range(len(wordToGuess))]
        # wordBlanks = createWordBlanks(wordToGuess)
        
        print(userBoard)
        print(wordBlanks)

        userGuess = askUser(wordToGuess)
        if validateGuess(wordToGuess, userGuess) == True: # Player got the guess right, fill in the correct blank
            print("DEBUG STATEMENT LINE 108: Valid Guess.")
            # fillInBlank(wordBlanks, wordToGuess, userGuess) # Update the wordBlanks string to display the correct information 
        else: # player got the guess wrong, add to the hangman board
            print("DEBUG STATEMENT LINE 108: Invalid Guess.")
            numGuesses += 1
            
            if numGuesses == 6:
                break
        

        

# displayIntro()
# while True:
# startGame()

# temp = createWordBlanks("Joe")
# fillInBlank(temp)

for i in range(0, len(HANGMAN_BOARDS)):
    print(HANGMAN_BOARDS[i])