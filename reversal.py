while True:
    userinput = int(input("Please enter a integer of at least 2 digits but no more than 11 digits or type -1 to exit: "))
    if userinput == -1:
        break
    elif userinput < 10:
        print("Invalid input, please enter a integer of at least 2 digits.")
    elif userinput > 99999999999:
        print("Invalid input, please enter a integer of less than 11 digits.")
    else:
        integerreversed = 0
        while userinput > 0:
            holder = userinput % 10
            integerreversed = (integerreversed * 10) + holder
            userinput = userinput // 10
        print("Reversed: " + str(integerreversed))