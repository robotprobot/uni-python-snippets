columns = int(input("How many columns would you like? "))
rows = int(input("How many rows would you like? "))

for row in range(rows):
    for column in range(columns):
        print("*", end=" ")
    print(" ")

