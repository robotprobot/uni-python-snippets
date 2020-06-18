integer1 = int(input("Please enter the first integer: "))
integer2 = int(input("Please enter the second integer: "))
operator = input("Please enter an operator (+, -, /, *): ")

if operator == "+":
    sum = integer1 + integer2

elif operator == "-":
    sum = integer1 - integer2

elif operator == "/":
    sum = integer1 / integer2

elif operator == "*":
    sum = integer1 * integer2

else:
    print("Incorrect operator!")

print("Result: " + str(sum))
