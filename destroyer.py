import re
formattingrule = re.compile(r'[^\d ]+')
destroyerplacement = [[3, 2], [4, 2]]

def map_print():
    map = [[0, 1, 2, 3, 4, 5],
        [1, '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
        [2, ' ', ' ', ' ', ' ', ' '],
        [3, ' ', ' ', ' ', ' ', ' '],
        [4, ' ', ' ', ' ', ' ', ' '],
        [5, ' ', ' ', ' ', ' ', ' ']]

    for i in range(len(map)):
        for j in range(len(map[i])):
            print('{:4}'.format(map[i][j]))
        print()

def coordinate_request():
    coordinatesacceptable = False
    while coordinatesacceptable == False:
        userinput = input("Please enter coordinates (along first then down, for example: 1 2): ")
        userinput = formattingrule.sub('', userinput)
        userinput = userinput.split()
        coordinate1 = 0
        coordinate2 = 0

        if not userinput:
            print("Please enter two coordinate numbers")
        elif 5 >= int(userinput[0]) >= 1:
            coordinate1 = int(userinput[0])
            if len(userinput) < 2:
                print("Please enter two coordinate numbers")
            elif 5 >= int(userinput[1]) >= 1:
                coordinate2 = int(userinput[1])
            else:
                print("Coordinate 2 is not acceptable. Must be between 1 and 5")
        else:
            print("Coordinate 1 is not acceptable. Must be between 1 and 5")

        if coordinate1 > 0 and coordinate2 > 0:
            coordinatesacceptable = True
            finalcoordinates = [[coordinate1], [coordinate2]]
            return finalcoordinates

def new_game():
    map_print()


new_game()

