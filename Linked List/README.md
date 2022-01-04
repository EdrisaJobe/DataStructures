# Linked List
|Access| Insertion|Deletion |Description |
|------|-------|------------|------------|
O(n)    |O(1)   |O(n)       | A linear data structure that is used to hold data in individual objects called nodes. Main purpose is for the efficient **insertion and deletion** methods, can be used alongsides stacks and queues. 

 

# 🛠️ Step-by-step

**The class Node**
```
# Just a blueprint for implementing the data structure you want
# Node class that has a constructor to initialize data and nextNode
# Classes should be named with caps to make them easy to read
class Node:
    
    # initializing the self convention(variable), making it known that it takes instance of its class
    # data is also stored, data is simply the value of the Node
    def __init__(self, data):
        
        # defining data to equal itself
        self.data = data
        # referencing other nodes within the list
        self.nextNode = None # None is null, empty
```
**The class LinkedList**
```
# Linkedlist class that takes in inserting a Node from head and inserting a Node from the last Node
class LinkedList:
    def __init__(self):
        
        # setting head to null because list is empty until data is added
        self.head = None
        # no amount of Nodes are set yet therefore it starts empty
        self.numNodes = 0
```
**Insertion at head - O(1)**
```
    # Inserting a Node at the beginning, takes O(1) because the list always start from the head
    def insert_start(self, data):
        
        # increment the reference value by 1 for every new item added
        self.numNodes = self.numNodes + 1
        # we now check to see if the Node is the head Node
        new_node = Node(data)
        
        # seeing if the head is empty
        # not is a logical operator, returns True when an expression is False (checks to see if two vars point to same obj in memory)
        # True and True = True, True and False = False, False and False = False
        if not self.head:
            # the head is now the new node
            self.head = new_node
        else:
            # making the added new node the new head
            new_node.nextNode = self.head
            # update the head node to now be the new_node
            self.head = new_node
```
**Insertion at tail - O(n)**
```
    # Inserting a Node at the end, O(n) linear time because it has to pass each Node to tget to the end (linear search)
    def insert_end(self, data):
        
        # similar to inserting, we have to start from the head and work our way up
        self.numNodes = self.numNodes + 1 
        new_node = Node(data)
        
        # points to the head of the list
        actual_node = self.head
        
        # finding the last node of the list, if the Node being searched is not null -> keep searching for the end
        while actual_node.nextNode is not None:
            
            # update actual_node, hopping from node to node: [3] -> [4] -> [6] -> [actual_node] -> null
            actual_node = actual_node.nextNode
        
        # inserts the Node into the new assigned value new_node at the end
        actual_node.nextNode = new_node
```
**Removing an item**
```
# removing specific data from within the list
    # [2]->[4]->[1]->[3]->null | w\if we remove element [1] we set element [4] to point to ->[3]
    def remove(self, data):
        
        # if the head is empty
        if self.head is None:
            
            # we return whatever is in the list
            return
        
        # set the actual_node to the head
        actual_node = self.head
        # 
        previous_node = None
        
        # we search for the item we want to delete by making sure the head is not empty and has data
        while actual_node is not None and actual_node.data != data:
            
            # we consider the next previous element the head
            previous_node = actual_node
            
            # after removal, we make the next item the new head
            actual_node = actual_node.nextNode
        
        # if the head is empty
        # search miss - the item is not present in the list
        if actual_node is None:
            return
        
        # update the size of list after removal
        self.numNodes = self.numNodes - 1
        
        # if the previous head is empty (getting rid of the given Node
        if previous_node is None:
             
             # give the head Node a new Node
             self.head = actual_node.nextNode 
        else:
            
            # reset the previous Node to be the head
            previous_node.nextNode = actual_node.nextNode
```
**Array size and traverse**
```
# the size of the list
    def arrSize(self):
        
        # get the number of nodes
        return self.numNodes
    
    # traversing through the list and storing a ref to the actual_node at the beginning 
    def traverse(self):
        
        actual_node = self.head
        
        # not at the end of linklist
        while actual_node is not None:
            
            print(actual_node.data)
            actual_node = actual_node.nextNode

```
**Inserting/Printing out data**
```
# inserting a random set of data within the list        
linked_list = LinkedList()

# inserting at beginning - O(1)
linked_list.insert_start(4)
linked_list.insert_start(3)
linked_list.insert_start(7)

# inserting at end O(n)
linked_list.insert_end(10)

linked_list.traverse()
```






