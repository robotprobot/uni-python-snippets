import random

correctlyguessedletterstotal = 0
incorrectlyguessedletterstotal = 0
correctlyguessedletters = []
incorrectlyguessedletters = []
started = False

def generate_word():
    wordlist = ["guard", "clean", "grain", "foregoing", "thunder", "lyrical", "surround", "whispering", "wrestle", "team", "somber", "noise", "injure", "glorious", "test", "peep", "thumb", "yoke", "meat", "fearful", "secret", "carriage", "heat", "servant"]
    selectedwordindex = random.randint(0, len(wordlist)-1)
    word = str((wordlist[selectedwordindex]))
    return word

def enter_word():
    acceptableword = False
    while acceptableword == False:
        inputtedword = input("Please enter a word (no numbers!): ")
        if any(str.isdigit(character) for character in inputtedword) or len(inputtedword) < 1:
            acceptableword = False
            print("Not a suitable entry, please enter one letter and no numbers!")
        else:
            acceptableword = True
            word = inputtedword
            print()
    return word

def start_game(word):
    print("Game of Hangman started, try guessing!")
    print()
    print("_ " * len(word))

def check_guess(userguess, incorrectlyguessedletters, word):
    if word.__contains__(userguess):
        return "CORRECT"
    else:
        if incorrectlyguessedletters.__contains__(userguess):
            return "INCORRECT"
        else:
            incorrectlyguessedletters.append(userguess)
            return "INCORRECT"

def word_guessed():
    print()
    print("You successfully guessed the word!")
    print("It took you " + str(incorrectlyguessedletterstotal + correctlyguessedletterstotal) + " tries to solve it.")

def guess_routine(word, suitableentry=False):
        print()
        print()
        print("Incorrect guesses")
        print(", ".join(incorrectlyguessedletters))
        print()
        while suitableentry != True:
            userguess = input("Please enter your guess: ")
            if any(str.isdigit(character) for character in userguess):
                suitableentry = False
                print("Not a suitable entry, please enter one letter.")
            else:
                userguess = userguess[0]
                suitableentry = True
        return userguess

def rerun_print(word, correctlyguessedletters, guessstate):
    guessedletters = 0
    if guessstate == "CORRECT":
        print("""

You guessed correctly.
""")
        for letter in word:
            if letter == userguess:
                if correctlyguessedletters.__contains__(letter):
                    break
                else:
                    guessedletters += 1
        for letter in word:
            if letter == userguess:
                if correctlyguessedletters.__contains__(letter):
                    print(letter, end=" ")
                else:
                    correctlyguessedletters.append(letter)
                    print(letter, end=" ")
            if letter != userguess:
                if correctlyguessedletters.__contains__(letter):
                    print(letter, end=" ")
                else:
                    print("_ ", end="")

    elif guessstate == "INCORRECT":
        print("""

You guessed incorrectly.
""")
        for letter in word:
            if correctlyguessedletters.__contains__(letter):
                print(letter, end=" ")
            elif letter != userguess:
                print("_ ", end="")
            else:
                print()
    return guessedletters

while started == False:
    genorpick = input("""
Generate a random word, or enter your own?
    
1) Generate
2) Enter your own word
""")
    if genorpick == "1":
        print()
        word = generate_word()
        started = True
    elif genorpick == "2":
        word = enter_word()
        started = True
    else:
        print("Please enter option 1 or 2.")
        started = False


start_game(word)

while correctlyguessedletterstotal < len(word):
    userguess = guess_routine(word)
    guesscheck = check_guess(userguess, incorrectlyguessedletters, word)
    if guesscheck == "CORRECT":
        amountcorrect = rerun_print(word, correctlyguessedletters, guessstate="CORRECT")
        correctlyguessedletterstotal = correctlyguessedletterstotal + amountcorrect
    else:
        incorrectlyguessedletterstotal += 1
        rerun_print(word, correctlyguessedletters, guessstate="INCORRECT")

word_guessed()