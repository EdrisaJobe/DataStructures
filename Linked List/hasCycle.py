def hasCycle(head):
    # Function to detect if a linked list has a cycle
    
    # Initialize two pointers at the head of the list
    fast = head  # Fast pointer will move two nodes at a time
    slow = head  # Slow pointer will move one node at a time

    # Continue until fast pointer reaches end of list
    # We need to check both fast and fast.next because fast.next.next would cause an error if fast.next is None
    while fast and fast.next:
        
        # Move slow pointer one step forward
        slow = slow.next
        # Move fast pointer two steps forward
        fast = fast.next.next

        # If the two pointers meet, we've detected a cycle
        # This works because in a cyclic list, a faster pointer will eventually catch up to a slower one
        if slow == fast:
            return True
    
    # If we exit the loop, fast pointer reached the end, meaning there's no cycle
    return False