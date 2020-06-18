width = int(input("What do you want the width to be? "))
while 1==1:
    if width <= 1:
        print("Width cannot be less than 2!")
        width = int(input("What do you want the width to be? "))
    if width >= 41:
        print("Width cannot be greater than 40!")
        width = int(input("What do you want the width to be? "))
    else:
        break

for amount in range(width * 2):
    if amount <= width: # if still in top half
        numberofspaces = width - amount # calculate the amount of spaces needed
        numberofplacements = amount # calculate how many asterisks will need to be placed
        print(" " * numberofspaces + "* " * numberofplacements) # print the spaces and asterisks as calculated

    else: # if in bottom half
        numberofspaces = amount - width # calculate the amount of spaces needed
        numberofplacements = 2 * width - amount # calculate how many asterisks will need to be placed
        print(" " * numberofspaces + "* " * numberofplacements) # print the spaces and asterisks as calculated

