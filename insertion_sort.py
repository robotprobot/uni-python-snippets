inputamount = 5
sortedamount = -1
inputs = []
sortedinputs = []

for i in range(inputamount):
    userinput = int(input("Please enter integer number " + str(i + 1) + ": "))
    inputs.append(userinput)

for i in inputs:
    if len(sortedinputs) == 0:
        sortedinputs.insert(0, i)
        inputs.remove(i)
        sortedamount = sortedamount + 1
    elif i > sortedinputs[sortedamount]:
        sortedinputs.insert(sortedamount, i) # FAILS COMPLETELY.
        inputs.remove(i)
        sortedamount = sortedamount + 1
    elif i < sortedinputs[sortedamount]:
        sortedinputs.append(i)
        inputs.remove(i)
        sortedamount = sortedamount + 1


print(inputs)
print(sortedinputs)