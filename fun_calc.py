def ask_user_for_integers():
    userinput = input("Please enter two numbers: ").split()
    return userinput

def show_menu():
    print("""
    1) Add
    2) Subtract
    3) Multiply
    4) Divide
    5) Remainder
    """)

def ask_user_for_menu_choice():
    menuchoice = 0
    while menuchoice == 0 or menuchoice > 5:
        menuchoice = int(input("Please enter menu choice number: "))
    return menuchoice

def add(usernumber1, usernumber2):
    result = usernumber1 + usernumber2
    return result

def subtract(usernumber1, usernumber2):
    result = usernumber1 - usernumber2
    return result

def multiply(usernumber1, usernumber2):
    result = usernumber1 * usernumber2
    return result

def divide(usernumber1, usernumber2):
    result = usernumber1 / usernumber2
    return result

def remainder(usernumber1, usernumber2):
    result = usernumber1 % usernumber2
    return result

numbers = ask_user_for_integers()
usernumber1 = int(numbers[0])
usernumber2 = int(numbers[1])

show_menu()
menuchoice = ask_user_for_menu_choice()
if menuchoice == 1:
    print("Adding...")
    print(add(usernumber1,usernumber2))
if menuchoice == 2:
    print("Subtracting...")
    print(subtract(usernumber1,usernumber2))
if menuchoice == 3:
    print("Multiplying...")
    print(multiply(usernumber1,usernumber2))
if menuchoice == 4:
    print("Dividing...")
    print(divide(usernumber1,usernumber2))
if menuchoice == 5:
    print("Finding remainder...")
    print(remainder(usernumber1,usernumber2))
