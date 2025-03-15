class Node:
    # Define a Node class that will be used to create nodes in the binary search tree
    def __init__(self, value):

        self.value = value  # Store the value in the node
        self.left = None    # Initialize left child reference to None
        self.right = None   # Initialize right child reference to None
        
class BinarySearchTree:
    def search(root, target):
        # Method to search for a target value in the binary search tree

        if not root:
            # If the root is None (empty tree or reached a leaf), the target is not found
            return False

        if target > root.value:
            # If target is greater than current node's value, search in the right subtree
            return BinarySearchTree(root.right, target)
        elif target < root.value:
            # If target is less than current node's value, search in the left subtree
            return BinarySearchTree(root.left, target)
        else:
            # If target equals current node's value, we found it
            return True

ll = BinarySearchTree()