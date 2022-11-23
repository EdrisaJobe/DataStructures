#String Methods
test = "Hello World!"

print (len(test))
print (str(test))
print (test.upper())
print (test.lower())

#date, time, and substitution
from datetime import datetime
timeNow = datetime.now()
name = "Awesome"
age = 19

print ("\n" + str(timeNow))
print ('%02d/%02d/%04d' % (timeNow.month, timeNow.day, timeNow.year))
print ('%02d:%02d:%02d' % (timeNow.hour, timeNow.minute, timeNow.second))
print ('I am %s, also I am %s years old!' % (name, age))

#Escaping Char and Index
getIndex = "My name is Edrisa"[3]

print ('\nHello, I am Edrisa\'s friend!')
print (getIndex)

#Equations
float1 = 13.2
float2 = 12.1
result = float1 * float2
result2 = float1 % float2
result3 = float1 + float2
result4 = float1 - float2

print ("\nThe multiplication is: " + str(result))
print ("The remainder is: " + str(result2))
print ("The addition is: " + str(result3))
print ("The substraction is: " + str(result4))

#Defining a variable
def meet(building):
    print ("Meet me at the " + building)

def time(clock):
    print ("at " + clock)

meet("office")
time("10:00")

sentence = "\nThis is pretty cool."

def mainSentence():
    if sentence == "Not that cool...":
        print ("This didn't go well...")
        return True
    else:
        return False

def secondSentence():
    if sentence == "This is pretty cool...":
        print ("Yea, it really is!")
        return True
    else:
        return False

print (sentence)

#if, else, and return statements
result = 12

if result > 3:
    print ("\nHello, my name is Edrisa.")
elif result < 3:
    print ("Hello, I am not Edrisa!")
else:
    print ("I could or could not be Edrisa...")

#Grabs string characters
math = "\nEquation"[0]

print (math)

work = "Adventure"[0:7]

print (work)

#raw inputs and .isalpha
sentence = "This is a test run"

word = input("Enter a word: ")
print (word)

phrase = input("Enter a phrase: ")

if phrase.isalpha():
    print ("True, only characters.")
else:
    print ("There's no characters.")

#Squared
def squared(n):

    result = n ** 2
    print ("\n%d squares is: %d" % (n, result))
    return squared
#get output
squared(2)

#Cubed
def power(number):

    result = number * number * number
    print ("%d cumbed is %d" % (number, result))

power(3)

#Exponents
def power(base, exponent):

    result = base ** exponent
    print ("%d is the base, %d is the exponent and result is: %d" % (base, exponent, result))

power(4, 18)

#Import list
import math
inMath = dir(math)

import datetime
inDateTime = dir(datetime)

print ("\n" + str(inMath))
print ("\n" + str(inDateTime))

#List Override
items = []

items.append("hammer")
items.append("saw")
items.append("screwdriver")
items.append("drill")

#get the length of items
listItems = len(items)
print ("\nThere are %d items." % (listItems))
print (items)

#List Slicing
foods = ["apple", "mango", "pear", "strawberry", "orange"]

listFoods = foods[0:3]
listFoods = foods[2:4]
listFoods = foods[3:5]

#print foods in a new line
print ("\n" + str(listFoods))

#List after colon
everything = "truckcarsupercar"

car = everything[5:8] #everything between c and r
supercar = everything[8:] #everything after s
truck = everything[:5] #everything before c for "car"

print ("\n" + str(car))
print (supercar)
print (truck)

#Sorts the list
names = ["Mike", "Jav", "Kenny", "Edrisa", "Ndeye"]
numbers = [12, 23, 321, 33, 1, 8]

#sorts names from A - Z and numbers 1 - 9
names.sort()
print (names)

numbers.sort()
print(numbers)

#define items
items = {}

#Set each item equal to a price
items["Grudon"] = 14.32
items["Apple pie"] = 12.32
items["Spinach wine"] = 19.00
items["Salad"] = 5.35

itemLength = len(items)
print ("""\nThe items are %s.
There are a total of %d items.""" % (items, itemLength))

