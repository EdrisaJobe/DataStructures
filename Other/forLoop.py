#define a variable
items = ["apple", "mango", "pear", "orange"]

#prints all items in vertical order
for allItems in items:

    #lists items in order
    items.sort()
    print (allItems)

#define definitions
dictionary = {"car" : "a vehicle that moves with foru wheels.",
"fish" : "a marine animal.", 
"cow" : "associated with beef."}

for defined in dictionary:
    print ( "\n" + str(dictionary[defined]))

#Print out even #'s only
numbers = [1, 2, 4, 52, 316, 432, 43, 12, 11]

for n in numbers:
    if n % 2 == 0:
        print ("\n" + str(n))

#vertical printing
word = "Octopus"

for w in word:
    print ("\n" + str(w))

#prints "Octopus" vertically
print
print

#lists prices and stock
prices = {"Apple": 2, "Banana": 1, "Pear": 4, "Watermelon": 12}
stock = {"Apple": 22, "Banana": 82, "Pear": 12, "Watermelon": 65}

total = 0

for foods in prices:
  
    print ("\n" + str(foods))
    print ("Price: $%d" % (prices[foods]))
    print ("Stock: %d" % (stock[foods]))
    print ("\nThe total is: " + str(prices[foods] * stock[foods]))

