itemlist = [] # INITIALIZE AN EMPTY LIST
while len(itemlist) < 10:
    if len(itemlist) == 0:
        itemname = input("Please enter item 1: ")
        itemprice = float(input("Please enter the price: "))
        print()
        itemamount = 1
    else: # THIS CODE BLOCK EITHER SIDE JUST CHANGES THE NUMBER ON THE REQUEST TEXT
        itemamount = itemamount + 1
        itemname = input("Please enter item " + str(itemamount) + ": ")
        itemprice = float(input("Please enter the price: "))
        print()
    itemlist.append(itemname) # ADDS ITEM NAME TO A LIST IN THE MAIN LIST
    itemlist.append(itemprice) # ADDS ITEM PRICE TO THAT LIST IN THE MAIN LIST

iteminfoformat = [[itemlist[0], itemlist[1]], [itemlist[2], itemlist[3]], [itemlist[4], itemlist[5]],
                  [itemlist[6], itemlist[7]], [itemlist[8], itemlist[9]]] # MAIN LIST


def sort(input):
    return sorted(input, key=lambda input: input[1], reverse=True) # SORTS BY GIVING INPUT TO LAMBDA AND REVERSING THE RESULT


iteminfosorted = sort(iteminfoformat) # REQUEST SORT


print(f"""{iteminfosorted[0][0]}: {format(iteminfosorted[0][1], '.2f')}
{iteminfosorted[1][0]}: {format(iteminfosorted[1][1], '.2f')}
{iteminfosorted[2][0]}: {format(iteminfosorted[2][1], '.2f')}
{iteminfosorted[3][0]}: {format(iteminfosorted[3][1], '.2f')}
{iteminfosorted[4][0]}: {format(iteminfosorted[4][1], '.2f')}""") # PRINT THE LIST ITEMS IN THE EXPECTED ORDER (FIRST, SECOND ETC)