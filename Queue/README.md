# Queue - (FIFO)
|Access| Enqueue|Dequeue |Description |
|------|-------|------------|------------|
O(1)    |O(1) |O(n)       | A data type (str, int, float) that holds a linear sequence of items. Also referred to as FIFO meaning the first thing in is the first thing to be removed or added. Uses **Peek()** - Which shows the last item within a list. **Dequeue()** - Removes the first item added. **Enqueue()** - Adds items to the list. **is_empty()** - Boolean, checks if the stack is empty. e.g. 1DArray -> [1][2][3][4][5]

# 🛠️ Step-by-step

**Global queue class**
```
class Queue:
    
    def __init__(self):
        
        self.queue = []
```
**Enqueue function**
```
    # O(1) - adds an item to the list
    def push(self,data):
        # inserting an item within the list
        self.queue.append(data)
```
**Dequeue function**
```
    # O(n) - removes items at the beginning of the queue and shifts the new items to the left
    def dequeue(self):
        
        # getting rid of the the first item
        data = self.queue[0]
        del self.queue[0]
        return data
```
**Peek function**
```
    # O(1) - gets the first item on the list without removal
    def peek(self):
        return self.queue[0]
```
**Checking if queue is empty and checking size**
```
    # O(1) - returns True or False if the list is empty
    def is_empty(self):
        return self.queue == []

    # O(1) - just getting queue size
    def queueSize(self): 
        return len(self.queue)
```
















