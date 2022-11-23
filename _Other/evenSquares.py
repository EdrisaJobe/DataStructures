#Gets numbers even between 1 - 21 and squares all numbers even
evenSquared = [x ** 2 for x in range (1, 21) if (x ** 2) % 2 == 0]
print (evenSquared)

#Gets numbers not even between 1 - 21 and squares all numbers not even
notEvenSquared = [x ** 2 for x in range (1, 21) if (x ** 2) % 2 != 0]
print ("\n"), (notEvenSquared)