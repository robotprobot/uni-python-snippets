# ask user questions
while True:
    rentpermonth = float(input("What is your rent per month? "))
    if rentpermonth <= 9999.99:
        if rentpermonth >= 0:
            break;
    print("Invalid entry, must be a number between 0 and 9999.99")
    
while True:
    gaspermonth = float(input("What is your gas bill per month? "))
    if gaspermonth <= 9999.99:
        if gaspermonth >= 0:
            break;
    print("Invalid entry, must be a number between 0 and 9999.99")

while True:
    electricpermonth = float(input("What is your electric bill per month? "))
    if electricpermonth <= 9999.99:
        if electricpermonth >= 0:
            break;
    print("Invalid entry, must be a number between 0 and 9999.99")

while True:
    waterpermonth = float(input("What is your water bill per month? "))
    if waterpermonth <= 9999.99:
        if waterpermonth >= 0:
            break;
    print("Invalid entry, must be a number between 0 and 9999.99")

while True:
    counciltaxpermonth = float(input("What is your council tax per month? "))
    if counciltaxpermonth <= 9999.99:
        if counciltaxpermonth >= 0:
            break;
    print("Invalid entry, must be a number between 0 and 9999.99")

# run calculations
totalpermonth = rentpermonth + gaspermonth + electricpermonth + waterpermonth + counciltaxpermonth

# output
print(f"""
============================
Your expenses per month are:
RENT:            £ {rentpermonth}
GAS:             £ {gaspermonth}
ELECTRIC:        £ {electricpermonth}
WATER:           £ {waterpermonth}
COUNCIL TAX:     £ {counciltaxpermonth}
============================
You are paying
monthly:         £ {totalpermonth}
============================
""")
