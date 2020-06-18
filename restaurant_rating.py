userinput = 0
onestarvotes = 0
twostarvotes = 0
threestarvotes = 0
fourstarvotes = 0
fivestarvotes = 0

def pass_to_results(onestarvotes, twostarvotes, threestarvotes, fourstarvotes, fivestarvotes):
    namelist = ["One Star", "Two Stars", "Three Stars", "Four Stars", "Five Stars"]
    resultlist = [onestarvotes, twostarvotes, threestarvotes, fourstarvotes, fivestarvotes]
    print()
    print("FINAL RESULTS: ")
    row_format = "{:>15}" * (len(namelist) + 1)
    print(row_format.format("", *namelist))
    print(row_format.format("", *resultlist))
    totalresponses = onestarvotes + twostarvotes + threestarvotes + fourstarvotes + fivestarvotes
    totalratings = onestarvotes + (2 * twostarvotes) + (3 * threestarvotes) + (4 * fourstarvotes) + (5 * fivestarvotes)
    if totalresponses != 0:
        average = totalratings / totalresponses
        print()
        print("The average is: " + str(round(average, 2)) + " stars.")
        exit()
    else:
        print()
        print("No votes were cast.")
        exit()

while True:
    print()
    userinput = input("Please enter your vote (1-5): ")
    try:
        if userinput == "1":
            onestarvotes += 1
            print("Vote cast. Thank you!")
        elif userinput == "2":
            twostarvotes += 1
            print("Vote cast. Thank you!")
        elif userinput == "3":
            threestarvotes += 1
            print("Vote cast. Thank you!")
        elif userinput == "4":
            fourstarvotes += 1
            print("Vote cast. Thank you!")
        elif userinput == "5":
            fivestarvotes += 1
            print("Vote cast. Thank you!")
        elif userinput == "-1":
            pass_to_results(onestarvotes, twostarvotes, threestarvotes, fourstarvotes, fivestarvotes)
    except:
        print("Error")


