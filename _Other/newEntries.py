#define items
items = {}

#Set each item equal to a price
items["Grudon"] = 14.32
items["Apple pie"] = 12.32
items["Spinach wine"] = 19.00
items["Salad"] = 5.35

itemLength = len(items)
print ("""The items are %s.
There are a total of %d items.""" % (items, itemLength))