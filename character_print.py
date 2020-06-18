defaultnumber = 0


def ask_user_for_input(defaultnumber):
    while defaultnumber < 1:
        userinput = input("Please enter a letter and a positive number: ").split()
        userletterresult = userinput[0]
        usernumberresult = int(userinput[1])
        return usernumberresult, userletterresult


def print_characters(userinputresult):
    for i in range(userinputresult[0]):
        print(userinputresult[1], end="")
        print(" ", end="")


userinputresult = ask_user_for_input(defaultnumber)
print_characters(userinputresult)