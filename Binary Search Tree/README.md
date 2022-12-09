# Stack - (LIFO)
|Search| Insertion|Deletion|Description |
|------|-------|---|---------------|
O(logN)    |O(logN) |  O(logN)    | With an **Array** and **LinkedList** it takes O(n) time to search or remove an arbritrary item, we use a BST in order to make this process O(1) removing and searching **allowing to store items efficiently**. We start from the middle and check the left or right sub arrays for the item we're looking for. Left child smaller than parent, right child greater than parent. (**PRE, IN, POST orders)**

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
















