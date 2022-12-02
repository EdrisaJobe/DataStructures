class Node:
    
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.numNodes = 0
        
    def insertStart(self,data):
        
        self.numNodes = self.numNodes + 1
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node
    
    def insertEnd(self, data):
        
        self.numNodes = self.numNodes + 1
        new_node = Node(data)
        currNode = self.head
        
        while currNode.nextNode is not None:
            currNode = currNode.nextNode
        currNode.nextNode = new_node
    
    def reverse(self):
        
        currNode = self.head
        prevNode = None
        
        while currNode is not None:
            
            nextNode = currNode.nextNode
            currNode.nextNode = prevNode
            prevNode = currNode
            currNode = nextNode
        
        self.head = prevNode
    
    def remove(self, data):
        
        if self.head is None:
            return
        
        currNode = self.head
        prevNode = None
        
        while currNode is not None and currNode.data != data:
            
            prevNode = currNode
            currNode = currNode.nextNode
            
        if currNode is None:
            return
        
        self.numNodes = self.numNodes - 1
        
        if prevNode is None:
            self.head = currNode.nextNode
        else:
            prevNode.nextNode = currNode.nextNode
            
            
    def traverse(self):
        
        currNode = self.head
        
        while currNode is not None:
            print(currNode.data)
            currNode = currNode.nextNode

l = LinkedList()

l.insertStart(23)
l.insertStart(83)
l.insertStart(93)
l.insertStart(33)

l.insertEnd(44)
l.insertEnd(63)
l.insertEnd(14)

l.remove(14)

l.traverse()
print('Reverse: ')
l.reverse()

l.traverse()