"""
game: Hangman -- a python project
author: benrmay

"""
guessWord = 'benrmaygame'
knownWord = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
hangmanGraphic = ['''
________      
|      |
|      
|
|
|
''',
                  '''
________
|      |
|      O
|
|
|
''',
                  '''
________
|      |
|      O
|      |
|
|
''',
                  '''
________
|      |
|      O
|      |
|     / \
|
''',
                  '''
________
|      |
|     _O_
|      |
|     / \
|
''']

def startGame():
    print("Welcome to Hangman, a game created by benrmay.")
    startInput = input("Would you like to start the game? (y/n)")
    if startInput == 'n':
        print ("Well then, goodbye. See you next Wednesday.")
        return
    else:
        numGuesses = 0
        guessedCharList = []
        while numGuesses < 5:
            print(hangmanGraphic[numGuesses])
            print(knownWord)
            letter = input("Guess a letter: ")
            i = 0
            check = alreadyGuessedLetter(letter)
            if check == False:
                guessFlag = False
                for char in guessWord:
                    if letter == char:
                        knownWord[i] = letter
                        guessFlag = True
                    i = i + 1
                if guessFlag == False:
                    print("Woops, wrong letter.")
                    guessedCharList.append(letter)
                    numGuesses = numGuesses + 1
                elif guessFlag == True:
                    print("Congrats! You got at least a letter")
                    guessedCharList.append(letter)
            if isGameWon() == True:
                print("Congrats! You won the game!!!")
                print("The word was " + guessWord + ".")
                return
    
def alreadyGuessedLetter(letter):
    for char in knownWord:
        if letter == char:
            print("You already tried " + letter + ". Try again!")
            return True
    return False

def isGameWon():
    for char in knownWord:
        if char == '_':
            return False
    return True
