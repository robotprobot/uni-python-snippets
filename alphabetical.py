def inputrun(inputscomplete, stringlist):
    while inputscomplete < 5:
        userinput = input("Please enter string " + str(inputscomplete + 1) + ": ")
        stringlist.append(userinput)
        inputscomplete += 1
    return stringlist


inputscomplete = 0
stringlist = []
completedstringlist = inputrun(inputscomplete, stringlist)

completedstringlistsorted = sorted(completedstringlist)

print()
print(f"""Your strings in alphabetical order:
{completedstringlistsorted[0]}
{completedstringlistsorted[1]}
{completedstringlistsorted[2]}
{completedstringlistsorted[3]}
{completedstringlistsorted[4]}""")
