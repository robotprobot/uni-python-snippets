username = input("Please input your full name: ")

def name_initial_split(username):
    splitname = username.split()
    print()
    print("Your initials are: ", end="")
    for i in splitname:
        print(i[0][0], end="")
    print()

name_initial_split(username)