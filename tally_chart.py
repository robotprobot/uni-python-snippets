userinput = 0
candidate1votes = 0
candidate2votes = 0
candidate3votes = 0
candidate4votes = 0
candidate5votes = 0

def appfinish():
    resultandprint()
    exit()

def sort(input):
    return sorted(input, key=lambda x: x[1], reverse=True)

def resultandprint():
    candidatevotes = [[1, candidate1votes], [2, candidate2votes], [3, candidate3votes], [4, candidate4votes], [5, candidate5votes]]
    candidatevotessorted = sort(candidatevotes)

    print(f"""
    RESULTS:
    Candidate {candidatevotessorted[0][0]}: {candidatevotessorted[0][1]} votes.
    Candidate {candidatevotessorted[1][0]}: {candidatevotessorted[1][1]} votes.
    Candidate {candidatevotessorted[2][0]}: {candidatevotessorted[2][1]} votes.
    Candidate {candidatevotessorted[3][0]}: {candidatevotessorted[3][1]} votes.
    Candidate {candidatevotessorted[4][0]}: {candidatevotessorted[4][1]} votes.""")

while userinput != -1:
    print(f"""
    CANDIDATES:
    1) Candidate 1 - {candidate1votes} votes.
    2) Candidate 2 - {candidate2votes} votes.
    3) Candidate 3 - {candidate3votes} votes.
    4) Candidate 4 - {candidate4votes} votes.
    5) Candidate 5 - {candidate5votes} votes.
    """)
    userinput = int(input("Please enter the number for who you want to vote for: "))
    if userinput == 1:
        candidate1votes += 1
    elif userinput == 2:
        candidate2votes += 1
    elif userinput == 3:
        candidate3votes += 1
    elif userinput == 4:
        candidate4votes += 1
    elif userinput == 5:
        candidate5votes += 1
    elif userinput == -1:
        appfinish()
    else:
        print("Invalid candidate, no vote has been cast.")