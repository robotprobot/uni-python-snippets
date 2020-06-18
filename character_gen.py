import random
import math

# ask user what class they want to be
possibleclasses = ["WARRIOR", "WIZARD", "THIEF", "NECROMANCER"]
print("""Classses:
WARRIOR
WIZARD
THIEF
NECROMANCER
""")

characterclass = ""
while characterclass not in possibleclasses:
    characterclass = input("What class would you like to be? ").upper()

# prepare minimum stats for that class
if characterclass == "WARRIOR":
    minimumstrength = 15
    minimumintelligence = 0
    minimumwisdom = 0
    minimumdexterity = 12
    minimumconstitution = 10
elif characterclass == "WIZARD":
    minimumstrength = 0
    minimumintelligence = 15
    minimumwisdom = 10
    minimumdexterity = 10
    minimumconstitution = 0
elif characterclass == "THIEF":
    minimumstrength = 10
    minimumintelligence = 9
    minimumwisdom = 0
    minimumdexterity = 15
    minimumconstitution = 0
elif characterclass == "NECROMANCER":
    minimumstrength = 10
    minimumintelligence = 10
    minimumwisdom = 15
    minimumdexterity = 0
    minimumconstitution = 0

# generate stats
strength = random.randrange(3,18)
intelligence = random.randrange(3,18)
wisdom = random.randrange(3,18)
dexterity = random.randrange(3,18)
constitution = random.randrange(3,18)

# compare rolled with minimum and mark if too low, whilst also generating the deficit amount.

deficittotal = 0

if strength < minimumstrength:
    lowstrength = True
    strengthdeficit = strength - minimumstrength
    deficittotal = deficittotal + strengthdeficit
else:
    lowstrength = False

if intelligence < minimumintelligence:
    lowintelligence = True
    intelligencedeficit = intelligence - minimumintelligence
    deficittotal = deficittotal + intelligencedeficit
else:
    lowintelligence = False

if wisdom < minimumwisdom:
    lowwisdom = True
    wisdomdeficit = wisdom - minimumwisdom
    deficittotal = deficittotal + wisdomdeficit
else:
    lowwisdom = False

if dexterity < minimumdexterity:
    lowdexterity = True
    dexteritydeficit = dexterity - minimumdexterity
    deficittotal = deficittotal + dexteritydeficit
else:
    lowdexterity = False

if constitution < minimumconstitution:
    lowconstitution = True
    constitutiondeficit = constitution - minimumconstitution
    deficittotal = deficittotal + constitutiondeficit
else:
    lowconstitution = False

# print minimums and rolled
print(f""" You chose: {characterclass}

Minimum stats required for {characterclass}:
Strength: {minimumstrength}
Intelligence: {minimumintelligence}
Wisdom: {minimumwisdom}
Dexterity: {minimumdexterity}
Constitution: {minimumconstitution}

You rolled:
Strength: {strength}
Intelligence: {intelligence}
Wisdom: {wisdom}
Dexterity: {dexterity}
Constitution: {constitution}
""")

# alert to deficits
if lowstrength == True:
    print("TOO LOW STRENGTH! (Deficit of " + str(strengthdeficit) + ")")
if lowintelligence == True:
    print("TOO LOW INTELLIGENCE! (Deficit of " + str(intelligencedeficit) + ")")
if lowwisdom == True:
    print("TOO LOW WISDOM! (Deficit of " + str(wisdomdeficit) + ")")
if lowdexterity == True:
    print("TOO LOW DEXTERITY! (Deficit of " + str(dexteritydeficit) + ")")
if lowconstitution == True:
    print("TOO LOW CONSTITUTION! (Deficit of " + str(constitutiondeficit) + ")")

if lowstrength == True or lowintelligence == True or lowwisdom == True or lowdexterity == True or lowconstitution == True:
    print("""
You can now transfer points from other skills that are already above the minimum in a ratio of 2 points for 1 point.
You cannot take a skill below 3 points, however. 
""")
else:
    print("Stats OK. Character generation complete.")
    exit()

# allow conversion of points
print("This means you can currently take:")
if minimumstrength == 0:
    movablestrength = strength - 3
    print(str(movablestrength) + " from strength.")
elif minimumstrength > 0:
    movablestrength = strength - minimumstrength
    if movablestrength < 0:
        movablestrength = 0
        print(str(movablestrength) + " from strength.")

if minimumintelligence == 0:
    movableintelligence = intelligence - 3
    print(str(movableintelligence) + " from intelligence.")
elif minimumintelligence > 0:
    movableintelligence = intelligence - minimumintelligence
    if movableintelligence < 0:
        movableintelligence = 0
        print(str(movableintelligence) + " from intelligence.")

if minimumwisdom == 0:
    movablewisdom = wisdom - 3
    print(str(movablewisdom) + " from wisdom.")
elif minimumwisdom > 0:
    movablewisdom = wisdom - minimumwisdom
    if movablewisdom < 0:
        movablewisdom = 0
        print(str(movablewisdom) + " from wisdom.")

if minimumdexterity == 0:
    movabledexterity = dexterity - 3
    print(str(movabledexterity) + " from dexterity.")
elif minimumdexterity > 0:
    movabledexterity = dexterity - minimumdexterity
    if movabledexterity < 0:
        movabledexterity = 0
        print(str(movabledexterity) + " from dexterity.")

if minimumconstitution == 0:
    movableconstitution = constitution - 3
    print(str(movableconstitution) + " from constitution.")
elif minimumconstitution > 0:
    movableconstitution = constitution - minimumconstitution
    if movableconstitution < 0:
        movableconstitution = 0
        print(str(movableconstitution) + " from constitution.")

totalpoints = (movablestrength + movableintelligence + movablewisdom + movabledexterity + movableconstitution)
amountofnewpointspossible = math.trunc(totalpoints / 2)

print(f"""
totalling {str(totalpoints)} points available to transfer into {str(amountofnewpointspossible)} alternative points.
""")

if -deficittotal > amountofnewpointspossible:
    print("""Unfortunately, with your roll it is not possible to be this character. 
    Restart the program to try again.""")
    exit()

allowedskills = ["STRENGTH", "INTELLIGENCE", "WISDOM", "DEXTERITY", "CONSTITUTION"]
while lowstrength == True or lowintelligence == True or lowwisdom == True or lowdexterity == True or lowconstitution == True:
    print("""Please select two points to exchange to one point.
    You can say '2 wisdom' to take 2 from wisdom, or '1 wisdom' then '1 strength' to take one from wisdom and one from strength.
    Remember that you cannot take a skill below the minimum for that class or below three total.
    """)
    userselection = input().upper()
    userselectionwords = userselection.split()
    userskillamount = userselectionwords[0]
    userskillchoice = userselectionwords[1]
    if userskillchoice in allowedskills:
        if userskillchoice == "STRENGTH":
            movableskillpoints = movablestrength
        elif userskillchoice == "INTELLIGENCE":
            movableskillpoints = movableintelligence
        elif userskillchoice == "WISDOM":
            movableskillpoints = movablewisdom
        elif userskillchoice == "DEXTERITY":
            movableskillpoints = movabledexterity
        elif userskillchoice == "CONSTITUTION":
            movableskillpoints = movableconstitution

        if int(userskillamount) <= movableskillpoints:
            if 0 <= int(userskillamount) <= 2:
                print("Taking " + str(userskillamount) + " from " + str(userskillchoice))

            else:
                print("You cant take " + str(userskillamount) + " from " + str(userskillchoice))
        else:
            print("You cant take " + str(userskillamount) + " from " + str(userskillchoice))
    else:
        print("Incorrect skill, please try again.")