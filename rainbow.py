colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

while True:
    userinput = int(input("Please enter a number between 1 and 7, or -1 to quit. "))
    if userinput == -1:
        exit()
    elif userinput < 1:
        print("Invalid entry")
    elif userinput > 7:
        print("Invalid entry")

    if userinput == 1:
        print(colors[0])

    elif userinput == 2:
        print(colors[1])

    elif userinput == 3:
        print(colors[2])

    elif userinput == 4:
        print(colors[3])

    elif userinput == 5:
        print(colors[4])

    elif userinput == 6:
        print(colors[5])

    elif userinput == 7:
        print(colors[6])