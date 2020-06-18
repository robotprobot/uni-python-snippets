import random

while True:
    throwone = random.randint(1,6)
    throwtwo = random.randint(1,6)

    print("Threw a " + str(throwone) + " and a " + str(throwtwo))

    if throwone == throwtwo:
        print("Matched! Dice one was " + str(throwone) + " and dice two was " + str(throwtwo) + ".")
        break