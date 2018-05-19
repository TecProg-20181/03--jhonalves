import random
import string
import timeit
from datetime import datetime

#variables with words list
WORDLIST_PT = "palavras.txt"
WORDLIST_EN = "words.txt"
LOG_FILE = "log.txt"
# 'abcdefghijklmnopqrstuvwxyz'
ALL_LETTERS = string.ascii_lowercase
GUESSES = 8

log_file = open(LOG_FILE, 'a')

def loadWords(mode):
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print "Loading word list from file..."
    start = timeit.default_timer()
    if mode == 'pt':
        # inFile: file
        try:
            inFile = open(WORDLIST_PT, 'r', 0)
        except IOError:
            print '\nTheres a problem oppening the ', WORDLIST_PT, ' file.'
            print '\nExiting...'
            exit()
    elif mode == 'en':
        # inFile: file
        try:
            inFile = open(WORDLIST_EN, 'r', 0)
        except IOError:
            print '\nTheres a problem oppening the ', WORDLIST_EN, ' file.'
            print '\nExiting...'
            exit()
    stop = timeit.default_timer()

    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    #print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord():
    guessed = ''

    return guessed

#print options menu and get choosen option
def printMenu():
    optionsList = [1, 2, 3]
    optionFailure = True
    optionIsNumber = True

    while optionFailure:
        print 'To play in Portuguese press 1'
        print 'To play in English press 2'
        print 'To quit press 3'
        print 'Choose: '
        try:
            option = input()
        except NameError:
            print '\nHey, enter a number to choose an option\n'
            option = 0
            optionIsNumber = False
        if option in optionsList:
            optionFailure = False
        else:
            if optionIsNumber:
                print '\nHey, the options available are 1, 2 and 3!\n'
            else:
                optionIsNumber = True
            optionFailure = True

    return option

def printPlayingMenu(lenght, differentLetters):
    print '\n-------------'
    print '\nLets play!'
    print 'I am thinking of a word that is', lenght, 'letters long.'
    print 'This word has ', differentLetters, ' different letters.'
    print '\n-------------\n'

def getLetter(available):
    print 'Available letters', available
    letter = raw_input('Please guess a letter: ')

    return letter

def updateGuessed(letter, secretWord, lettersGuessed):
    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_'

    return guessed

def checkWin(secretWord, lettersGuessed):
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print 'Congratulations, you won!\n'
    else:
        print 'Sorry, you ran out of guesses. The word was ', secretWord, '.\n'

def checkDifferentLetters(secretWord):
    differentLetters = []
    for letter in secretWord:
        if letter not in differentLetters:
            differentLetters.append(letter)

    quantitieDifferentLetters = len(differentLetters)
    return quantitieDifferentLetters

def changeWord(guesses, differentLetters):
    if differentLetters > guesses:
        print '\nYour secret word has more different letters than your number of guesses'

        playOnList = [1, 2]
        playOnFailure = True
        playOnIsNumber = True

        while playOnFailure:
            print 'Press 1 to play on'
            print 'Press 2 to get a new word: '
            try:
                playOn = input()
            except NameError:
                print '\nHey, enter a number to choose an option\n'
                playOn = 0
                playOnIsNumber = False
            if playOn in playOnList:
                playOnFailure = False
            else:
                if playOnIsNumber:
                    print '\nHey, the options available are 1 and 2!\n'
                else:
                    playOnIsNumber = True
                playOnFailure = True
    else:
        playOn = 1

    return playOn

def guessing(secretWord, lettersGuessed, guesses):
    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'

        available = ALL_LETTERS
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        letter = getLetter(available)

        if letter in lettersGuessed:
            guessed = updateGuessed(letter, secretWord, lettersGuessed)

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = updateGuessed(letter, secretWord, lettersGuessed)

            print 'Good Guess: ', guessed
        else:
            guesses -=1
            lettersGuessed.append(letter)

            guessed = updateGuessed(letter, secretWord, lettersGuessed)

            print 'Oops! That letter is not in my word: ',  guessed
        print '\n------------\n'

    checkWin(secretWord, lettersGuessed)

    return guesses

def play(mode):
    playOn = 2

    while playOn == 2:
        guesses = GUESSES
        lettersGuessed = []
        secretWord = loadWords(mode).lower()
        secretWordLenght = len(secretWord)
        differentLetters = checkDifferentLetters(secretWord)

        playOn = changeWord(guesses, differentLetters)

        if playOn == 1:
            printPlayingMenu(secretWordLenght, differentLetters)
            guessesLeft = guessing(secretWord, lettersGuessed, guesses)
        elif playOn == 2:
            print '\nHold on, lets get you a new word...'
        else:
            pass

    logGuesses = 'In play - Guesses: ' + str(guesses) + '\n'
    logguessesLeft = 'In play - Guesses left: ' + str(guessesLeft) + '\n'
    logLettersGuessed = 'In play - Letters guessed: ' + str(lettersGuessed) + '\n'
    logSecretWord = 'In play - Secret word: ' + str(secretWord) + '\n'
    logSecretWordLenght = 'In play - Secret word lenght: ' + str(secretWordLenght) + '\n'
    log_file.write(logGuesses)
    log_file.write(logguessesLeft)
    log_file.write(logLettersGuessed)
    log_file.write(logSecretWord)
    log_file.write(logSecretWordLenght)

def hangman():
    start = datetime.now()
    start_log = 'Execution starting at ' + str(start) + '\n'
    #print start_log
    log_file.write('-----------------------\n')
    log_file.write(start_log)

    finish = False
    print '** Welcome to the game, Hangam! **\n'

    while(finish == False):
        option = printMenu()

        #play in portuguese
        if option == 1:
            play('pt')
            log_file.write('In hangman - Choosen option: Portuguese\n')
        #play in english
        elif option == 2:
            play('en')
            log_file.write('In hangman - Choosen option: English\n')
        #quit game
        elif option == 3:
            print '\nSee ya...'
            log_file.write('In hangman - Choosen option: Exit\n')
            finish = True
        #prints blank line before next menu
        else:
            print ''
            log_file.write('In hangman - Unknown error in hangman method\n')

#calls main function
hangman()
