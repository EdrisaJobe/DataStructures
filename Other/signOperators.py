#Sign operators
bool1 = 1 == 2
bool2 = 100 > 12
bool3 = 9 <= 9
bool4 = 14 >= 21
bool5 = 4**3 == 68 #4 cubed is 64
bool6 = 4**2 == 16 #4 squared is 16

#Print out the results
print (bool1)
print (bool2)
print (bool3)
print (bool4)
print (bool5)
print (bool6)

#Operators
test1 = ("\n" + str(1 < 2 and 3 > 5)) #both must be true to be TRUE
test2 = 12 > 5 or 2 < 1 #One or the other has to be true to be TRUE
test3 = not 2 > 1 #Since 2 is greater than 1 it is True, therefore FALSE
test4 = not 2 < 1 #Not true therefore it's TRUE
test5 = not not 4 < 2 #Double not acts as a positive

#results
print (test1)
print (test2)
print (test3)
print (test4)
print (test5)