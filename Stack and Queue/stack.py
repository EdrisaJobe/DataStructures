#Stack is LIFO CONSTANT O(1), takes the last thing and brings it out first, used with .append() & .pop() cmd
#One pointer at the end of the list on the inserted item

#empty array names
names = []

#adding to the list
names.append("Edrisa")
names.append("Modou")

#print names
print(names)

#pop last item inserted, pointer is now on "Edrisa"
names.pop() or names.pop(1) #both do the same task
 
print(names)