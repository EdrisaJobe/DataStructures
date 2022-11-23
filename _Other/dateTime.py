#imports datetime
from datetime import datetime
timeNow = datetime.now()
timeNow2 = datetime.now()

#Prints out full date
print (timeNow)
print (timeNow.month)
print (timeNow.day)
print (timeNow.year)

#Can also be formatted:
print(timeNow2, timeNow2.day, timeNow2.month, timeNow2.year)

#Also formatted as:
print ('%02d/%02d/%04d' % (timeNow2.month, timeNow2.day, timeNow2.year))
print ('%02d-%02d-%04d' % (timeNow2.month, timeNow2.day, timeNow2.year))

#Hrs Mins and Secs
print ('%02d:%02d:%02d' % (timeNow2.hour, timeNow2.minute, timeNow2.second))

#All together in a row:
print ('%02d/%02d/%04d'  %(timeNow2.hour, timeNow2.minute, timeNow2.second) + ' %02d:%02d:%02d' % (timeNow2.hour, timeNow2.minute, timeNow2.second))
