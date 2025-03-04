# This is an implementation of a Doubly Linked List with dummy head/tail nodes
# Visual representation of the initial empty list:
#
# Head (-1) <-> Tail (-1)
#
# After adding nodes:
# Head (-1) <-> Node1 <-> Node2 <-> ... <-> NodeN <-> Tail (-1)

class Node:
    def __init__(self, value):
        self.value = value  # The data stored in the node
        self.next = None    # Reference to next node
        self.prev = None    # Reference to previous node

class LinkedList:
    def __init__(self):
        # Create dummy head and tail nodes with value -1
        # Visual: Head (-1) <-> Tail (-1)
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value):
        # Insert at front (after head)
        # Before: Head <-> A <-> B
        # After:  Head <-> NewNode <-> A <-> B
        newNode = Node(value)
        newNode.prev = self.head
        newNode.next = self.head.next
        
        self.head.next.prev = newNode
        self.head.next = newNode

    def insertEnd(self, value):
        # Insert at end (before tail)
        # Before: A <-> B <-> Tail
        # After:  A <-> B <-> NewNode <-> Tail
        newNode = Node(value)
        newNode.next = self.tail
        newNode.prev = self.tail.prev
        
        self.tail.prev.next = newNode
        self.tail.prev = newNode

    def removeFront(self):
        # Remove first real node (after head)
        # Before: Head <-> A <-> B <-> Tail
        # After:  Head <-> B <-> Tail
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    def removeEnd(self):
        # Remove last real node (before tail)
        # Before: Head <-> A <-> B <-> Tail
        # After:  Head <-> A <-> Tail
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def traverse(self):
        # Print all nodes from head to tail
        curr = self.head.next
        while curr != self.tail:
            print(curr.value, " <-> ", end="")
            curr = curr.next
        print("Tail")

# Example usage that creates this list:
# Head <-> 99 <-> 79 <-> 23 <-> 54 <-> 87 <-> Tail
ll = LinkedList()

ll.insertFront(23)  # Head <-> 23 <-> Tail
ll.insertFront(79)  # Head <-> 79 <-> 23 <-> Tail  
ll.insertFront(99)  # Head <-> 99 <-> 79 <-> 23 <-> Tail

ll.insertEnd(54)    # Head <-> 99 <-> 79 <-> 23 <-> 54 <-> Tail
ll.insertEnd(87)    # Head <-> 99 <-> 79 <-> 23 <-> 54 <-> 87 <-> Tail

ll.traverse()       # Prints: 99 <-> 79 <-> 23 <-> 54 <-> 87 <-> Tail