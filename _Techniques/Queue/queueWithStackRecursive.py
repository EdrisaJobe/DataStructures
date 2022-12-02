class Queue:

    def __init__(self):

        self.stack = []

    # O(1), adding an item within the list
    def enqueue(self, data):
        return self.stack.append(data)

    def dequeue(self):

        # O(1) - get the first item in the stack if length is 1
        if len(self.stack) == 1:
            return self.stack.pop()

        # O(n) - we keep popping until we find the last item
        item = self.stack.pop()

        # O(n) - recursively call the function until we find the 1ast item inserted
        dequeuedItem = self.dequeue()

        # O(n) - when the item is found we insert the new order of items 1by1 again
        self.stack.append(item)

        # return the found items
        return dequeuedItem
        
    
    def size(self):
        return len(self.stack)
    
q = Queue()

q.enqueue(12)
q.enqueue(43)
q.enqueue(98)
q.enqueue(102)

print('Size before:')
print(q.size())

print('\nNew order:')
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print('\nSize after:')
print(q.size())
