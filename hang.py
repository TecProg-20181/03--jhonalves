import random
import string

WORDLIST_PT = "palavras.txt"
WORDLIST_EN = "words.txt"

def loadWords(mode):
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    if mode == 'pt':
        # inFile: file
        inFile = open(WORDLIST_PT, 'r', 0)
    elif mode == 'en':
        # inFile: file
        inFile = open(WORDLIST_EN, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []

#    for letter in secretWord:
#        if letter in secretLetters:
#            secretLetters.append(letter)
#        else:
#            pass

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

def printMenu():
    print 'To play in Portuguese press 1'
    print 'To play in English press 2'
    print 'To quit press 3'
    option = raw_input('Choose: ')

    return option

def printPlayingMenu(lenght):
    print '\n'
    print 'Lets play!'
    print 'I am thinking of a word that is', lenght, 'letters long.'
    print '\n-------------\n'

def guessing(secretWord, lettersGuessed, guesses):
    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        print 'You have ', guesses, 'guesses left.'

        available = getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Good Guess: ', guessed
        else:
            guesses -=1
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'

def hangman():

    guesses = 8
    lettersGuessed = []
    finish = False
    print 'Welcome to the game, Hangam!'

    while(finish == False):
        option = printMenu()

        if option == '1':
            secretWord = loadWords('pt').lower()
            printPlayingMenu(len(secretWord))
            guessing(secretWord, lettersGuessed, guesses)
        elif option == '2':
            secretWord = loadWords('en').lower()
            printPlayingMenu(len(secretWord))
            guessing(secretWord, lettersGuessed, guesses)
        elif option == '3':
            print 'See ya...'
            finish = True

hangman()
