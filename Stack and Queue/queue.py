# FIFO CONSTANT O(1), first in first out (dequeue & enqueue), .append() is used to insert the array 
# two pointers, front of the list and one at the end of the previous inserted item (empty space)
# stores n-1 elements

names = []

#pointer one is on "edrisa", pointer two is after "aisha" on the empty space
names.append("edrisa")
names.append("momodou")
names.append("aisha")

#poping the first item and printing out results / pointer in front is now on "momodou"
names.pop(0)
print(names)


