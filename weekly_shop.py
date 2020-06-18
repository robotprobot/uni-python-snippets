amountpeach = int(input("How many peaches you want to buy: "))
pricepeach = int(input("How much one peach costs: "))

amountbeans = int(input("How many cans of beans you want to buy: "))
pricebeans = int(input("How much one can of beans costs: "))

amountchicken = int(input("How many packets of chicken pieces you want to buy: "))
pricechicken = int(input("How much one packet of chicken pieces costs: "))

amountsocks = int(input("How many pairs of socks you want to buy: "))
pricesocks = int(input("How much one pair of socks costs: "))

amountwater = int(input("How many bottles of water you want to buy: "))
pricewater = int(input("How much one bottle of water costs: "))


totalamountofitems = amountpeach + amountbeans + amountchicken + amountsocks + amountwater
totalcostofitems = (pricepeach * amountpeach) + (pricebeans * amountbeans) + (pricechicken * amountchicken) + (pricesocks * amountsocks) + (pricewater * amountwater)

print("~~ Total amount of items purchased: " + str(totalamountofitems))
print("~~ Total cost of weekly shop: " + str(totalcostofitems))
