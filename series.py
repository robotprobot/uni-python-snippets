number1 = input("Please enter number 1: ")
number2 = input("Please enter number 2: ")
number3 = input("Please enter number 3: ")
number4 = input("Please enter number 4: ")
number5 = input("Please enter number 5: ")

numbers = [number1, number2, number3, number4, number5]

positives = 0
negatives = 0

for item in numbers:
    if int(item) > 0:
        positives = positives + int(item)
    if int(item) < 0:
        negatives = negatives + int(item)

print("Sum of positive numbers: " + str(positives))
print("Sum of negative numbers: " + str(negatives))