while True:
    userinput = int(input("Please enter 5 integers: "))
    if len(str(userinput)) == 5:
        break
    else:
        print("5 digits only please!")

reverseduserinput = 0
while userinput > 0:
    holder = userinput % 10
    reverseduserinput = (reverseduserinput * 10) + holder
    userinput = userinput // 10
print(str(reverseduserinput))

