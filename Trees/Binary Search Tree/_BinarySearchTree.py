class Node:
    # Define a Node class that will be used to create nodes in the binary search tree
    def __init__(self, value):
        # Store the value in the node
        self.value = value
        # Initialize left child reference to None
        self.left = None
        # Initialize right child reference to None
        self.right = None
        
class BinarySearchTree:

    def insert(self, root, value):
        # Check if the tree is empty or we've reached a leaf node
        if root is None:
            return Node(value)
            
        # If the value is greater than the root's value, insert into the right subtree
        if value > root.value:
            # Recursively insert into the right subtree and update the right child reference
            root.right = self.insert(root.right, value)
        # If the value is less than the root's value, insert into the left subtree
        elif value < root.value:
            # Recursively insert into the left subtree and update the left child reference
            root.left = self.insert(root.left, value)

        # Return the root node after insertion
        return root


    def search(self, root, target):
        # Method to search for a target value in the binary search tree

        # Check if we've reached the end of a branch or the tree is empty
        if not root:
            # If the root is None (empty tree or reached a leaf), the target is not found
            return False

        # If target is greater than current node's value, search in the right subtree
        if target > root.value:
            # Recursively search in the right subtree
            return self.search(root.right, target)
        # If target is less than current node's value, search in the left subtree
        elif target < root.value:
            # Recursively search in the left subtree
            return self.search(root.left, target)
        # If target equals current node's value, we found it
        else:
            # Return True to indicate the target was found
            return True

    def findMin(self, root):
        # Method to find the minimum value in the binary search tree
        
        # Start at the root node
        curr = root
        # Keep traversing to the left child as long as it exists
        # (In a BST, the minimum value is always in the leftmost node)
        while curr and curr.left:
            # Move to the left child
            curr = curr.left
        # Return the node with the minimum value
        return curr

    def remove(self, root, value):
        # Check if we've reached the end of a branch or the tree is empty
        if not root:
            return None

        # If value is greater than root's value, remove from right subtree
        if value > root.value:
            # Recursively remove from right subtree and update right child reference
            root.right = self.remove(root.right, value)
        # If value is less than root's value, remove from left subtree
        elif value < root.value:
            # Recursively remove from left subtree and update left child reference
            root.left = self.remove(root.left, value)
        # If value equals root's value, this is the node to remove
        else:
            # Case 1: Node has no left child, replace with right child
            if not root.left:
                return root.right
            # Case 2: Node has no right child, replace with left child
            elif not root.right:
                return root.left
            # Case 3: Node has both children
            else:
                # Find the minimum value in the right subtree
                minNode = self.findMin(root.right)
                # Replace current node's value with the minimum value
                root.value = minNode.value
                # Remove the node with the minimum value from the right subtree
                root.right = self.remove(root.right, minNode.value)
        # Return the modified root
        return root

# Create a new binary search tree
ll = BinarySearchTree()

# Insert values into the tree
ll.insert(32)
ll.insert(21)
ll.insert(55)
ll.insert(12)