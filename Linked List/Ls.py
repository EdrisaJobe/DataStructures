class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.nextNode = None

class LinkedList:
    
    def __init__(self):
        
        self.head = None
        self.numOfNodes = 0
        
    def insert_start(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node
    
    def insert_end(self,data):
        
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)
        
        actual_node = self.head
        
        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode
        
        actual_node.nextNode = new_node
    
    def arrSize(self):
        return self.numOfNodes
    
    def traverse(self):
        
        actual_node = self.head
        
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode

linked_list = LinkedList()

linked_list.insert_start(4)
linked_list.insert_start(3)
linked_list.insert_start(7)
linked_list.insert_end(10)

linked_list.traverse()
