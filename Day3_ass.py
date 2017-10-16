price_of_ice_cream = 2.5
total_money_you_have = 12
ice_cream_you_can_afford = total_money_you_have / price_of_ice_cream
balance_money = total_money_you_have - (ice_cream_you_can_afford * price_of_ice_cream)
extra_money_needed = price_of_ice_cream - balance_money

print "The price of ice cream is", price_of_ice_cream, "each."
print "You have total of", total_money_you_have,"Dollars."
print "With that, you can only buy", ice_cream_you_can_afford, "ice creams."
print "Your balance money will be", balance_money,
print "You need", extra_money_needed, "to buy additional ice cream."
