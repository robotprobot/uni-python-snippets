minutes = int(input("How many minutes? "))

callcost = float(minutes * 0.15)
vat = float((callcost / 100) * 20)
total = float(callcost + vat)

print(f"""
Number of minutes: {minutes}
Basic call charge: {callcost}
VAT Due: {vat}
Total Bill: {total}
""")

