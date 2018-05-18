import random
import string

#variables with words list
WORDLIST_PT = "palavras.txt"
WORDLIST_EN = "words.txt"


def loadWords(mode):
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print "Loading word list from file..."
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

def getAvailableLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase


    return available

#print options menu and get option choosen
def printMenu():
    print 'To play in Portuguese press 1'
    print 'To play in English press 2'
    print 'To quit press 3'
    option = raw_input('Choose: ')

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
        print 'Press 1 to play on'
        playOn = raw_input('Press 2 to get a new word: ')
    else:
        playOn = '1'

    return playOn

def guessing(secretWord, lettersGuessed, guesses):
    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'

        available = getAvailableLetters()
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

def play(mode):
    playOn = '2'

    while playOn == '2':
        guesses = 8
        lettersGuessed = []
        secretWord = loadWords(mode).lower()
        secretWordLenght = len(secretWord)
        differentLetters = checkDifferentLetters(secretWord)

        playOn = changeWord(guesses, differentLetters)

        if playOn == '1':
            printPlayingMenu(secretWordLenght, differentLetters)
            guessing(secretWord, lettersGuessed, guesses)
        elif playOn == '2':
            print '\nHold on, lets get you a new word...'
        else:
            print 'aaaaaaaaaaa'

def hangman():

    finish = False
    print '** Welcome to the game, Hangam! **\n'

    while(finish == False):
        option = printMenu()

        #play in portuguese
        if option == '1':
            play('pt')
        #play in english
        elif option == '2':
            play('en')
        #quit game
        elif option == '3':
            print '\nSee ya...'
            finish = True
        #prints blank line before next menu
        else:
            print ''
            pass

#calls main function
hangman()
