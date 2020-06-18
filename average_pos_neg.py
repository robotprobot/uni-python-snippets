firstnumber = int(input("Please enter first number: "))
secondnumber = int(input("Please enter second number: "))
thirdnumber = int(input("Please enter third number: "))
fourthnumber = int(input("Please enter fourth number: "))
fifthnumber = int(input("Please enter fifth number: "))
sixthnumber = int(input("Please enter sixth number: "))
seventhnumber = int(input("Please enter seventh number: "))
eighthnumber = int(input("Please enter eighth number: "))
ninthnumber = int(input("Please enter ninth number: "))
tenthnumber = int(input("Please enter tenth number: "))

numberlist = [firstnumber, secondnumber, thirdnumber, fourthnumber, fifthnumber,
           sixthnumber, seventhnumber, eighthnumber, ninthnumber, tenthnumber]

positivetotal = 0
negativetotal = 0

for number in numberlist:
    if number > 0:
        positivetotal = positivetotal + number
    elif number < 0:
        negativetotal = negativetotal + number

print("")

if positivetotal == 0:
    print("No positives were entered.")
else:
    print("Total amount of positives: " + str(positivetotal))
    print("Average postive: " + str(positivetotal / 10))

if negativetotal == 0:
    print("No negatives were entered.")
else:
    print("Total amount of negatives: " + str(negativetotal))
    print("Average negative: " + str(negativetotal / 10))