def preOrder(root):
    """
    Iterative pre-order traversal of a binary tree.
    
    Pre-order traversal visits nodes in the order: root node, left subtree, right subtree.
    
    This implementation uses a stack to track nodes:
    1. Process the current node
    2. Push right child to stack (to process after left subtree)
    3. Move to the left child and repeat
    4. When we can't go left anymore, pop from stack and process
    
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree
    
    Visualization:
        1
       / \
      2   3     Pre-order: 1 -> 2 -> 4 -> 5 -> 3
     / \
    4   5
    
    Process:
    - Visit 1, push 3 to stack, move to 2
    - Visit 2, push 5 to stack, move to 4
    - Visit 4, no children, pop 5 from stack
    - Visit 5, no children, pop 3 from stack
    - Visit 3, no children, stack empty, done
    """
    if not root:
        return
        
    stack = []
    curr = root

    while curr or stack:
        if curr:    
            print(curr.val)  # Process current node

            if curr.right:
                stack.append(curr.right)  # Save right child for later
            curr = curr.left  # Move to left child
        else:
            curr = stack.pop()  # No more left children, process right

# Recursive pre-order traversal
def preOrderRecur(root):
    """
    Recursive pre-order traversal of a binary tree.
    
    The recursive approach naturally implements the node-left-right order:
    1. First process the current node
    2. Then recursively traverse the left subtree
    3. Finally recursively traverse the right subtree
    
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree (due to call stack)
    """
    if not root:
        return []
        
    result = []
    result.append(root.val)  # Process current node
    result.extend(preOrderRecur(root.left))  # Traverse left subtree
    result.extend(preOrderRecur(root.right))  # Traverse right subtree
    return result

# Example usage
# result = preOrderRecur(root)
# print(result)