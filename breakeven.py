cost_per_item = float(20.00)
sale_price_of_item = float(40.00)
fixed_costs = float(50000.00)

# break even calculation
sale_minus_item_cost = sale_price_of_item - cost_per_item
breakeven = fixed_costs / sale_minus_item_cost

print("Cost to produce one item: " + str(cost_per_item))
print("Sale price of the item: " + str(sale_price_of_item))
print("Profit per item sold: " + str(sale_price_of_item - cost_per_item))
print("Fixed costs: " + str(fixed_costs))

print("Break even at: " + str(breakeven))