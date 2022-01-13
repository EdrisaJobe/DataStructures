# Stack
|Access| Insertion tail|Deletion tail |Description |
|------|-------|------------|------------|
O(1)    |O(1) |O(1)       | A data type (str, int, float) that holds a linear sequence of items. Also referred to as LIFO meaning the last thing in is the first thing to be removed or added. Uses **Peek()** - Which shows the last item within a list. **Pop()** - Removes the last item added. **Push()** - Add an item at the top of the list. **is_empty()** - Boolean, checks if the stack is empty. e.g. 1DArray -> [1][2][3][4][5]

# 🛠️ Step-by-step

**Global stack class**
```
class Stack:
    
    def __init__(self):
        # empty 1D array
        self.stack = []
```
**Push or append function**
```
    # O(1) - adds an item to the list
    def push(self,data):
        # inserting an item within the list
        self.stack.append(data)
```
**Pop function**
```
    # O(1) - removes the last item within a list
    def pop(self):
        
        if self.stackSize() < 1:
            return -1
        
        # getting the last item
        data = self.stack[-1]
        # removing the last item
        del self.stack[-1]
        return data
```
**Peek function**
```
    # O(1) - returns an item w/o removing it
    def peek(self):
        
        if self.stackSize() < 1:
            return 'This list is empty.'
        
        return self.stack[-1]
```
**Checking if stack is empty and checking size**
```
    # O(1) - returns True or False if the list is empty
    def is_empty(self):
        return self.stack == []

    def stackSize(self):
        return len(self.stack)
```
















