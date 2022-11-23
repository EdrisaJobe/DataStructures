#Allows you to enter any work or value in console
title = "This is a test!"

sayHi = input("Say hi in your language: ")
print (sayHi)

#Allows you to enter only CHARACTERS not ints or floats
thisString = input("Enter a word: ")

if thisString.isalpha():
    print ("Yes, only characters!")
else:
    print("No, there's no characters.")
