def inOrder(root):
    """
    Iterative in-order traversal of a binary tree.
    
    In-order traversal visits nodes in the order: left subtree, current node, right subtree.
    
    This implementation uses a stack to track nodes:
    1. We continuously push left children onto the stack until we reach a null node
    2. When we can't go left anymore, we pop from the stack, process the node
    3. Then we move to the right child and repeat the process
    
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree
    """
    stack = []
    curr = root

    while curr or stack:
        # Traverse to the leftmost node
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            # When we can't go left, process current node and go right
            curr = stack.pop()
            print(curr.val)
            curr = curr.right


# Recursively
def inOrderRecur(root):
    """
    Recursive in-order traversal of a binary tree.
    
    The recursive approach naturally implements the left-node-right order:
    1. First recursively traverse the left subtree
    2. Then process the current node
    3. Finally recursively traverse the right subtree
    
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree (due to call stack)
    """
    if not root:
        return

    inOrderRecur(root.left)  # Traverse left subtree
    print(root.val)          # Process current node
    inOrderRecur(root.right) # Traverse right subtree

# Example usage
# inOrderRecur(root)
# To collect results instead of printing, use a list:
# res = []
# def inOrderRecur(root, res):
#     if root:
#         inOrderRecur(root.left, res)
#         res.append(root.val)
#         inOrderRecur(root.right, res)
#     return res