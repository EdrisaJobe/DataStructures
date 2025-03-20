from collections import deque

def breadthFirstSearch(root):
    """
    Breadth-First Search (BFS) traversal of a binary tree.
    
    BFS visits nodes level by level, from top to bottom, left to right.
    
    This implementation uses a queue to track nodes:
    1. Start with the root node in the queue
    2. For each level, process all nodes in the current queue
    3. Add all children to the queue for the next level
    
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(w) where w is the maximum width of the tree
    
    Visualization:
        1         Level 0: 1
       / \
      2   3       Level 1: 2 -> 3
     / \   \
    4   5   6     Level 2: 4 -> 5 -> 6
    
    Process:
    - Start with node 1 in queue
    - Process level 0: visit 1, add 2 and 3 to queue
    - Process level 1: visit 2, visit 3, add 4, 5, and 6 to queue
    - Process level 2: visit 4, visit 5, visit 6
    """
    
    queue = deque()                  
    res = []
    
    if root:                         # Check if the root exists
        queue.append(root)           # Add root to the queue to start BFS

    while len(queue) > 0:            # Continue until queue is empty
        
        level = []                   # Initialize a list to store values at current level

        for _ in range(len(queue)):  # Process all nodes at current level

            curr = queue.popleft()   # Remove the first node from queue
            level.append(curr.val)   # Add current node's value to current level

            if curr.left:            # If current node has a left child
                queue.append(curr.left)  # Add left child to queue for next level
            if curr.right:           # If current node has a right child
                queue.append(curr.right) # Add right child to queue for next level
        
        res.append(level)            # Add the completed level to result
    
    return res                       # Return the level-by-level traversal result
            

#     1         level = 0
#    / \
#   2   3       level = 1
#  / \   \
# 4   5   6     level = 2
