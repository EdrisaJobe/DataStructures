def postOrder(root):
    """
    Iterative post-order traversal of a binary tree.
    
    Post-order traversal visits nodes in the order: left subtree, right subtree, root node.
    
    This implementation uses two stacks to track nodes and their visited state:
    1. We push nodes onto the stack with a visited flag
    2. When we encounter a node that hasn't been visited, we push it back with visited=True
       and also push its children to be processed first
    3. When we encounter a visited node, we process it
    
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree
    
    Visualization:
        1
       / \
      2   3     Post-order: 4 -> 5 -> 2 -> 3 -> 1
     / \
    4   5
    
    Process:
    - Push 1 (unvisited) to stack
    - Pop 1, mark as visited, push back 1 (visited), push 3, push 2
    - Process 2, 3, then finally 1
    """
    if not root:
        return
        
    stack = [root]
    visit = [False]

    while stack:
        curr, visited = stack.pop(), visit.pop()

        if curr:
            if visited:
                print(curr.val)  # Process current node
            else:
                stack.append(curr)
                visit.append(True)
                stack.append(curr.right)
                visit.append(False)
                stack.append(curr.left)
                visit.append(False)

def postOrderRecur(root):
    """
    Recursive post-order traversal of a binary tree.
    
    The recursive approach naturally implements the left-right-node order:
    1. First recursively traverse the left subtree
    2. Then recursively traverse the right subtree
    3. Finally process the current node
    
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree (due to call stack)
    
    Visualization:
        1
       / \
      2   3     Post-order: 4 -> 5 -> 2 -> 3 -> 1
     / \
    4   5
    """
    if not root:
        return
        
    postOrderRecur(root.left)   # Traverse left subtree
    postOrderRecur(root.right)  # Traverse right subtree
    print(root.val)             # Process current node