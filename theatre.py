adultprice = 10.50
childprice = 7.30
concessionsprice = 8.40
postandpackcharge = 2.34

freeadultqualifies = "false"
freeadultplaces = 0
totalremoved = 0
finaltotal = 0

over100deduction = 0
over100discountmessage = "10% discount on any order over £100 (after any other discounts applied)."

numberofadults = int(input("How many adults under 65 years old? "))
numberofconcessions = int(input("How many adults over 65 years old? "))
numberofchildren = int(input("How many children? "))

if numberofchildren > 0 and numberofadults == 0 and numberofconcessions == 0:
    print("Error, children must be accompanied by an adult.")
    exit()

totalamountofpeople = numberofadults + numberofconcessions + numberofchildren
if totalamountofpeople == 0:
    print("Error, no people.")
    exit()

while 1==1:
    collectiontype = str(input("How would you like to receive the tickets? <COLLECTION/DELIVERY> ")).upper()
    if collectiontype == "COLLECTION":
        break;
    if collectiontype == "DELIVERY":
        break;
    else:
        print("Invalid input, please enter Collection or Delivery.")

if numberofchildren >= 10:
    freeadultplaces = freeadultplaces + 1
    remainingnumberofchildren = numberofchildren - 10
    while remainingnumberofchildren >= 10:
        freeadultplaces = freeadultplaces + 1
        remainingnumberofchildren = remainingnumberofchildren - 10
        if remainingnumberofchildren < 10:
            break;

basetotal = (adultprice * numberofadults) + (concessionsprice * numberofconcessions) + (childprice * numberofchildren)
totalwithfreespaces = basetotal
if collectiontype == "COLLECTION":
    postandpackcharge = float(0.00)

if freeadultplaces == 0:
    discountmessage = "No discounts."
elif freeadultplaces > 0:
    freeadultqualifies = "true";
    discountmessage = "Qualifies for " + str(freeadultplaces) + " free adult ticket(s) (excluding concessions)."
    numberofadultstoremovefrom = numberofadults
    while freeadultplaces > 0 and numberofadultstoremovefrom > 0:
        numberofadultstoremovefrom = numberofadultstoremovefrom - 1
        freeadultplaces = freeadultplaces - 1
        totalremoved = totalremoved + adultprice
        totalwithfreespaces = basetotal - totalremoved
        if freeadultplaces == 0:
            break;

if totalwithfreespaces > 100:
    finaltotal = (totalwithfreespaces / 100 * 90)
    over100deduction = (totalwithfreespaces / 100 * 10)
else:
    finaltotal = totalwithfreespaces

print(f"""
--------------------------------------------------------------------------------   
AMOUNT OF ADULTS UNDER 65:                     {numberofadults} adults.
                                               Individual ticket price: {'£{:.2f}'.format(float(adultprice))}
                                               total: {'£{:.2f}'.format(float((adultprice * numberofadults)))}
                                           
AMOUNT OF ADULTS OVER 65:                      {numberofconcessions} concessions.
                                               Individual ticket price: {'£{:.2f}'.format(float(concessionsprice))}
                                               total: {'£{:.2f}'.format(float((concessionsprice * numberofconcessions)))}
                                                                                        
AMOUNT OF CHILDREN:                            {numberofchildren} children.
                                               Individual ticket price: {'£{:.2f}'.format(float(childprice))}
                                               total: {'£{:.2f}'.format(float((childprice * numberofchildren)))}
                                               
BASE PRICE OF ALL TICKETS BEFORE DISCOUNTS:    {'£{:.2f}'.format(float(basetotal))}
--------------------------------------------------------------------------------   
DISCOUNTS:
""")
if freeadultqualifies == "true":
    print(discountmessage)
    print("-" + '£{:.2f}'.format(float(totalremoved)))
    print("")
if over100deduction > 0:
    print(over100discountmessage)
    print("-" + '£{:.2f}'.format(float(over100deduction)))
elif over100deduction == 0 and freeadultqualifies == "false":
    print("No discounts applicable for this booking.")
print(f"""--------------------------------------------------------------------------------                                            
ORDER TYPE:                                    {collectiontype}

BASE PRICE OF ALL TICKETS AFTER DISCOUNTS:     {'£{:.2f}'.format(float(finaltotal))}
POSTAGE AND PACKAGING:                         {'£{:.2f}'.format(postandpackcharge)}
--------------------------------------------------------------------------------
FINAL TOTAL:                                   {'£{:.2f}'.format(float(finaltotal + postandpackcharge))}
--------------------------------------------------------------------------------
""")

