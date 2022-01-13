# pop() removes last item within the list while 
# peek() doesn't remove the item just returns it
# append() pushes, adds an item within the list
# LIFO - Last In First Out
# Stack Memory: data type that stores active functions and local variables
# Pros: fast access/small size/no fragmentation
# Heap Memory: the size of the memory is way larger than stack (can store more items), can store objects
# Pros: large size/slow access/stores obj/may be fragmented(unused memory)


class Stack:
    
    def __init__(self):
        # empty 1D array
        self.stack = []
    
    # O(1) - adds an item to the list
    def push(self,data):
        # inserting an item within the list
        self.stack.append(data)
    
    # O(1) - removes the last item within a list
    def pop(self):
        
        if self.stackSize() < 1:
            return -1
        
        # getting the last item
        data = self.stack[-1]
        # removing the last item
        del self.stack[-1]
        return data
    
    # O(1) - returns an item w/o removing it
    def peek(self):
        
        if self.stackSize() < 1:
            return 'This list is empty.'
        
        return self.stack[-1]
    
    # O(1) - returns True or False if the list is empty
    def is_empty(self):
        return self.stack == []

    def stackSize(self):
        return len(self.stack)

stack = Stack()

stack.push(32)
stack.push(22)
stack.push(11)
stack.push(99)

print('The size of the stack is: %d' % stack.stackSize())
print('\nThe item poped was: %d' % stack.pop())
print('\nThe item poped was: %d' % stack.pop())
print('\nThe item poped was: %d' % stack.pop())
print('\nThe new size of the stack is: %d' % stack.stackSize())
print('\nLast item not removed but shown is: %s' % stack.peek())
print('\nNo items in stack? %s' % stack.is_empty())
