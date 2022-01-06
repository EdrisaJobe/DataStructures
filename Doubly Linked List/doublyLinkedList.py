# starting with a class Node, followed by the main LinkedList class
# Doubly | null <- [] <-> [] <-> [] -> null
class Node:
    
    def __init__(self, data):
        
        # data will take in whatever amount we give it
        self.data = data
        
        # we want each Node to reference to one another
        self.next = None
        self.previous = None
        
class DoublyLinkedList:
    
    def __init__(self):
        
        # head and tail are empty until a Node has been added
        self.head = None
        self.tail = None
    
    # inserts items at the end - O(1) runtime
    def insert_end(self, data):
        
        # set new_node to the Node object
        new_node = Node(data)
        
        # if the head is empty, we know the new_node is the head 
        if self.head is None:
            
            # set both the head and tail to the new_node
            # head points at first item, tail points at last item
            self.head = new_node
            self.tail = new_node
        
        # when there is at least 1 item within the list
        # we keep insering items at the tail
        else:
            # the previous node is the tail, we have to set the next node to be the new tail
            new_node.previous = self.tail
            self.tail.next = new_node
            
            # update the new_node to now be the tail
            self.tail = new_node
    
    # we can traverse the list in both directions | null -> [] -> [] -> [] -> null
    def traverse_forward(self):
        
        # the actual_node start from the head
        actual_node = self.head
        
        # loop when the actual_node is not empty, print out the actual_node
        while actual_node is not None:
            
             # .data is added to insert the items given
            print('%d' % actual_node.data)
            
            # move from node to node within the list forwards
            actual_node = actual_node.next
    
    # we can traverse the list in both directions | null <- [] <- [] <- [] <- null
    def traverse_backward(self):
        
        # the actual_node starts from the tail
        actual_node = self.tail
        
        # loop when the actual_node is not empty, print out the actual_node
        while actual_node is not None:
            
            print('%d' % actual_node.data)
            
            # move from node to node within the list backwards
            actual_node = actual_node.previous

# function call
if __name__ == '__main__':
     listL = DoublyLinkedList()
     
     listL.insert_end(1)
     listL.insert_end(5)
     listL.insert_end(7)
     listL.insert_end(3)
     
     listL.traverse_forward()
     print("----")
     listL.traverse_backward()