import random
import sys

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
/|\  |
     |
    ===''',
   '''
 +---+
 O   |
/|\  |
/    |
    ===''',
   '''
 +---+
 O   |
/|\  |
/ \  |
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



def startGame():
    gameIsRunning = True
    
    numChances = 6
    
    missedLetters = []  # List of letters guessed that were incorrect
    correctLetters = [] # List of letters guessed that were correct

    wordToGuess = random.choice(LIST_OF_EASY_WORDS) # Select a word
    
    while gameIsRunning == True:
        if len(missedLetters) == numChances:
            print("GameOver!")
            sys.exit()

        userBoard = HANGMAN_BOARDS[len(missedLetters)]
        wordBlanks = '_' * len(wordToGuess)

        print(userBoard)
        print(wordBlanks)

        userGuess = askUser(wordToGuess)

        if validateGuess(wordToGuess, userGuess) == True: # Player got the guess right, fill in the correct blank
            print("VALID GUESS")
            correctLetters.append(userGuess)
        else: # player got the guess wrong, add to the hangman board
            print("INVALID GUESS")
            if userGuess in missedLetters:
                print(f"You already guessed {userGuess}. Try again.")
            else:
                missedLetters.append(userGuess)
            
            
            
# displayIntro()
# while True:
startGame()

# temp = createWordBlanks("Joe")
# fillInBlank(temp)
