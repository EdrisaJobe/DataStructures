# Node class represents each element in the linked list
class ListNode:
    def __init__(self, val):
        self.val = val      # Stores the value of the node
        self.next = None    # Points to the next node, initially None

# Main LinkedList class that manages the list operations
class LinkedList:
    def __init__(self):
        # Creates a dummy head node with value -1
        # This dummy node simplifies operations like deletion from start
        self.head = ListNode(-1)
        # Tail points to the last node, initially same as head
        self.tail = self.head
    
    def insertEnd(self, val):
        # Creates new node and adds it after tail
        self.tail.next = ListNode(val)
        # Updates tail to point to the new last node
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
        # Traverse to the node just before the one we want to remove
        while i < index and curr:
            i += 1
            curr = curr.next
        
        # If we found the position and a node exists after it
        if curr and curr.next:
            # If removing the last node, update tail
            if curr.next == self.tail:
                self.tail = curr
            # Skip over the node we're removing
            curr.next = curr.next.next

    def print(self):
        # Start from first actual node (after dummy)
        curr = self.head.next
        # Print each node's value followed by arrow
        while curr:
            print(curr.val, " -> ", end="")
            curr = curr.next
        # Print newline at end
        print()
