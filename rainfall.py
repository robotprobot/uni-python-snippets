months = 12
monthstext = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
rainfall = []
for i in range(months):
    amount = int(input("Please enter rainfall for month " + str(monthstext[i]) + ": "))
    rainfall.append(amount)

highestrainfall = max(rainfall)

print()
while highestrainfall > 0:
    for i in rainfall:
        print("  ", end="")
        if i == highestrainfall:
            print("*", end="  ")

        elif i > highestrainfall:
            print("*", end="  ")

        elif i != highestrainfall:
            print("  ", end=" ")
    print()
    highestrainfall -= 1

for i in range(months):
    print(" ", end="")
    print(monthstext[i], end=" ")
print()