# FIFO - first item in is the first item removed
# useful for CPU scheduling such as determining when a process should execute or be on hold

class Queue:
    
    def __init__(self):
        
        self.queue = []
    
    # O(1) - boolean, sees if the queue is empty
    def is_empty(self):
        
        return self.queue == []
    
    # O(1) - adds data at the end of the 1D array | [1],[2],[3] ...
    def enqueue(self,data):
        
        return self.queue.append(data)
    
    # O(n) - removes items at the beginning of the queue and shifts the new items to the left
    # O(1) - if we pop from end
    def dequeue(self):
        
        # getting rid of the the first item
        data = self.queue[0]
        del self.queue[0]
        return data
    
    # O(1) - gets the first item on the list without removal
    def peek(self):
        return self.queue[0]

    # O(1) - just getting array size
    def queueSize(self):
        
        return len(self.queue)

queue = Queue()

queue.enqueue(23)
queue.enqueue(93)
queue.enqueue(63)
queue.enqueue(43)

print('Size before: %s' % queue.queueSize())
print('\nOld first: %s' % queue.peek())
print('\nItem removed: %s ' % queue.dequeue())
print('\nNew first: %s' % queue.peek())
print('\nIs queue empty? %s' % queue.is_empty())
print('\nSize after: %s ' % queue.queueSize())
