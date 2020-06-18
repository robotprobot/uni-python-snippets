username = input("Please input your full name: ")

def name_initial_split(username):
    splitname = username.split()
    print()
    print("Your initials are: ", end="")
    for i in splitname:
        if "-" in i:
            i = i.split("-")
            amount = len(i)
            for i in i:
                if amount > 1:
                    print(i[0][0] + "-", end="")
                else:
                    print(i[0][0] + ".", end="")
                amount -= 1
        else:
            print(i[0][0] + ".", end="")
    print()

