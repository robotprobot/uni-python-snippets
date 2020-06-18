def display_grid(guess1=None, guess2=None):
    print("  0 1 2 3")
    for row in range(4):
        print(row, end=" ")
        for col in range(4):
            if guess1 and guess1[0] == row and guess1[1] == col:
                print(game_grid[guess1[0]][guess1[1]], end=" ")
            elif guess2 and guess2[0] == row and guess2[1] == col:
                print(game_grid[guess2[0]][guess2[1]], end=" ")
            elif [row, col] in already_guessed:
                print("X", end=" ")
            else:
                print("*", end=" ")
        print()


def get_user_input():
    guess = [int(coord) for coord in input("Please enter coordinates: ").split()]

    while guess in already_guessed or len(guess) != 2:
        guess = [int(coord) for coord in input("Please enter coordinates: ").split()]

    return guess


def cards_match(guess1, guess2):
    return game_grid[guess1[0]][guess1[1]] == game_grid[guess2[0]][guess2[1]]


game_grid = [
    ['A', 'J', 'Q', 'K'],
    ['J', 'K', 'A', 'J'],
    ['K', 'Q', 'K', 'Q'],
    ['Q', 'A', 'J', 'A']
]

already_guessed = []

number_of_guesses = 0

while len(already_guessed) < 32:
    display_grid()

    guess1 = get_user_input()

    guess2 = guess1

    display_grid(guess1)

    while guess2 == guess1:
        guess2 = get_user_input()

    display_grid(guess1, guess2)

    if cards_match(guess1, guess2):
        already_guessed += [guess1, guess2]

    number_of_guesses += 1

print("You won! It took you {} turns".format(number_of_guesses))