# Node class represents a single node in a linked list
class Node:
    def __init__(self):
        # Each node has a next pointer, initially set to None
        self.next = None

def reverseLinkedList(head=Node()):
    # prev keeps track of the previous node, starts as None since first node has no previous
    prev = None
    # curr points to current node being processed, starts at head of list
    curr = head

    # Continue until we reach end of list (curr becomes None)
    while curr:
        # Save reference to next node before we change curr.next
        temp = curr.next
        # Reverse the link - point current node's next to previous node
        curr.next = prev
        # Move prev pointer one step forward to current node
        prev = curr
        # Move current pointer one step forward to next node (saved in temp)
        curr = temp

    # prev is now pointing to the last node (new head of reversed list)
    return prev

# Note: This won't work with a list [1,2,3,4,5,6] but the output will be reversed
print(reverseLinkedList([1,2,3,4,5,6]))