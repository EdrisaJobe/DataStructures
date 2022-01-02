#gets a lits of items
items = ['Books', 'Apples', "Pens", 'Pencils']

#removes a specific word from the list
items.remove("Apples")
print(items)

#deletes an item within a list
items = {'Colors' : 'Yellow', 
'Black' : 'White', 
'Brown' : 'Green', 
'Orange' : 'Purple'}

#deletes from the list
del items['Green']
items['White'] = 'Tan'

print (items)