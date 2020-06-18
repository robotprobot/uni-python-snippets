import random

number = random.randint(1, 13)

if number == 1:
    print("You drew a Ace card!")
elif number in range(1, 11):
    print("You drew a " + str(number) + " card!")
elif number == 11:
    print("You drew a Jack card!")
elif number == 12:
    print("You drew a Queen card!")
elif number == 13:
    print("You drew a King card!")

while True:
    userthink = input(("Do you think that the next card will be higher or lower? ")).upper()
    if userthink == "HIGHER":
        secondnumber = random.randint(1, 13)
        if secondnumber == 1:
            print("You drew a Ace card!")
        elif secondnumber in range(1, 11):
            print("You drew a " + str(secondnumber) + " card!")
        elif secondnumber == 11:
            print("You drew a Jack card!")
        elif secondnumber == 12:
            print("You drew a Queen card!")
        elif secondnumber == 13:
            print("You drew a King card!")

        if secondnumber > number:
            print("You were correct! It was higher!")
        elif secondnumber < number:
            print("You were wrong, it was lower!")
        elif secondnumber == number:
            print("It wasnt higher or lower! It was the same!")

        break
    elif userthink == "LOWER":
        secondnumber = random.randint(1, 13)
        if secondnumber == 1:
            print("You drew a Ace card!")
        elif secondnumber in range(1, 11):
            print("You drew a " + str(secondnumber) + " card!")
        elif secondnumber == 11:
            print("You drew a Jack card!")
        elif secondnumber == 12:
            print("You drew a Queen card!")
        elif secondnumber == 13:
            print("You drew a King card!")

        if secondnumber < number:
            print("You were correct! It was lower!")
        elif secondnumber > number:
            print("You were wrong, it was higher!")
        elif secondnumber == number:
            print("It wasnt higher or lower! It was the same!")

        break
    else:
        print("Invalid input, enter Higher or Lower.")