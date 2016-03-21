"""
game: Hangman -- a python project
author: benrmay

"""
guessWordList = 'laser diagonal comfy myth dorsal biscuit hydrogen macaroni rubber darkness yolk exercise vegetarian shrew chestnut ditch wobble glitter neighborhood dizzy fire side retail drawback logo fabric mirror barber jazz migrate drought commercial dashboard bargain double download professor landscape ski goggles vitamin'.split()
hangmanGraphic = ['''
________      
|      |
|      
|
|
|
========
''',
                  '''
________
|      |
|      O
|
|
|
========
''',
                  '''
________
|      |
|      O
|      |
|
|
========
''',
                  '''
________
|      |
|      O
|      |
|     / \\
|
========
''',
                  '''
________
|      |
|     _O_
|      |
|     / \\
|
========
''']

import hangmanHelper #this file has the hangman pictures and the guess word list.
import random
    
def startGame():
    print("Welcome to Hangman, a game created by benrmay.")
    startInput = input("Would you like to start the game? (y/n)")
    if startInput == 'n':
        print ("Well then, goodbye. See you next Wednesday.")
        return
    else:
        guessWord = getGuessWord(guessWordList)
        knownWord = createKnownWord(guessWord)
        numGuesses = 0
        guessedCharList = []
        while numGuesses < 5:
            print(hangmanGraphic[numGuesses])
            printKnownWord(knownWord)
            letter = input("Guess a letter: ")
            i = 0
            check = alreadyGuessedLetter(letter, knownWord)
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
            if isGameWon(knownWord) == True:
                print("Congrats! You won the game!!!")
                print("The word was " + guessWord + ".")
                return
        print("You lost! Try again some other time.")
        print("The word was " + guessWord + ".")
        return
    
def alreadyGuessedLetter(letter, knownWord):
    for char in knownWord:
        if letter == char:
            print("You already tried " + letter + ". Try again!")
            return True
    return False

def isGameWon(knownWord):
    for char in knownWord:
        if char == '_':
            return False
    return True

def getGuessWord(guessWordList):
    return guessWordList[random.randint(0, len(guessWordList) - 1)]

def createKnownWord(guessWord):
    knownWord = []
    for char in guessWord:
        knownWord.append('_')
    return knownWord

def printKnownWord(knownWord):
    tempStr = ''.join(knownWord)
    print(" ".join(tempStr))
    return
