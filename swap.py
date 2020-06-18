def ask_user_for_integers():
    userinput = input("Please enter two numbers: ").split()
    return userinput


def swap_list(numbers):
    firstnumber = numbers[1]
    secondnumber = numbers[0]
    swappednumbers = [firstnumber, secondnumber]
    return swappednumbers


def print_results(numbers, swappednumbers):
    print("You entered: " + str(numbers[0]) + " " + str(numbers[1]) + ", swapped: " + str(swappednumbers[0]) + " " + str(swappednumbers[1]) + ".")


numbers = ask_user_for_integers()
swappednumbers = swap_list(numbers)
print_results(numbers, swappednumbers)