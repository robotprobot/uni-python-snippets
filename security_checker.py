menuchoiceacceptable = False
usernamesandpasswords = []

def new_user(usernamesandpasswords):
    print()
    usernameacceptable = False
    passwordconfirmed = False
    while usernameacceptable == False:
        username = input("Please enter a username to create: ")
        usernames = [item[0] for item in usernamesandpasswords]
        if usernames.__contains__(username):
            print()
            print("User already exists. Please try again.")
        else:
            usernameacceptable = True
    while passwordconfirmed == False:
        password = input("Please enter a password for that username: ")
        confirmpassword = input("Please confirm the password: ")
        if password == confirmpassword:
            if password[0].isnumeric():
                print()
                print("Password cannot start with a number.")
            else:
                if password.__contains__(" "):
                    print()
                    print("Password cannot have a space.")
                else:
                    if len(password) > 7:
                        passwordconfirmed = True
                    else:
                        print()
                        print("Password does not match length requirements. Must be at least 8 characters long.")
        else:
            print()
            print("Passwords do not match, please try again.")
    usernamesandpasswords.append([username, password])
    print("User setup complete. Returning to main menu.")

def existing_user():
    print()
    usernameacceptable = False
    passwordcorrect = False
    if len(usernamesandpasswords) == 0:
        print("No accounts have been setup. Switching to new user setup.")
        new_user(usernamesandpasswords)
        return
    while usernameacceptable == False:
        username = input("Please enter username: ")
        usernames = [item[0] for item in usernamesandpasswords]
        passwords = [item[1] for item in usernamesandpasswords]
        passwordattempts = 3
        if usernames.__contains__(username):
            usernameacceptable = True
            usernameindex = usernames.index(username)
            expectedpassword = passwords[usernameindex]
            while passwordcorrect == False:
                givenpassword = input("Please enter password for " + username + " (or -1 to cancel): ")
                if givenpassword == expectedpassword:
                    passwordcorrect = True
                    print("Welcome, " + username + "!")
                elif givenpassword == "-1":
                    print("Returning to main menu.")
                    break
                else:
                    print("Password incorrect.")
                    passwordattempts -= 1
                    if passwordattempts == 0:
                        print("Maximum amount of attempts reached. Exiting...")
                        exit()
                    else:
                        print(str(passwordattempts) + " attempt(s) remaining.")
        else:
            print("Username not found. Returning to main menu.")
            break

while menuchoiceacceptable == False:
    print("""
    1) New User
    2) Existing User
    """)
    userchoice = input("Please enter your menu choice: ")
    if userchoice == "1":
        new_user(usernamesandpasswords)
    elif userchoice == "2":
        existing_user()
    else:
        menuchoiceacceptable = False