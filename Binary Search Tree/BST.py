class Node:
    
    def __init__(self,data,parent):
        
        self.data = data
        
        # left and right children, and the parent Node
        self.left = None
        self.right = None
        self.parent = parent

class BinarySearchTree:

    def __init__(self):
        
        # the root is set to an empty
        self.root = None

    def insert(self,data):
        
        # if root is empty, we pass data into it
        if self.root is None:

            self.root = Node(data, None)
        else:
            
            # calls the isnert() funct, when we try to insert data
            self.insertNode(data, self.root)
            
    def insertNode(self, data, node):
        
        # we are traversing the left subtree
        if data < node.data:
            if node.left is not None:
                self.insertNode(data, node.left)
            else:
                node.left = Node(data, node)
                
        # we are traversing the right subtree
        else:
            if node.right is not None:
                self.insertNode(data, node.right)
            else:
                node.right = Node(data, node)
        
    def removeNode(self, data, node):
        
        if node is None:
            return
        
        # if the node is less than nodes data go left, else if greater go right
        if data < node.data:
            self.removeNode(data, node.left)
        elif data > node.data:
            self.removeNode(data, node.right)
        
        # otherwise we found the node we want removed and do specific removals
        else:
            
            # removing a single leaf node
            if node.left is None and node.right is None:
                print('Removing a leaf node... %d' % node.data)
                parent = node.parent
                
                # we set the parent node to be none after removal of child
                if parent is not None and parent.left == node:
                    parent.left = None
                if parent is not None and parent.right == node:
                    parent.right = None
                
                if parent is None:
                    self.root = None
                
                del node
            
            # removing a single right node, we set the edge to connect to the right child's left node
            elif node.left is None and node.right is not None:
                print('Removing a single right child...')
                parent = node.parent
                
                if parent:
                    if parent.left == node:
                        parent.left = node.right
                    if parent.right == node:
                        parent.right == node.right
                # if parent is None, update root node to be right node
                else:
                    self.root = node.right
                
                node.right.parent = parent
                del node
            
            # removing a single left node, we set the edge to connect to the left child's right node
            elif node.right is None and node.left:
                print('Removing a single left node...')
                parent = node.parent
                
                if parent:
                    if parent.left == node:
                        parent.left = node.left
                    if parent.right == node:
                        parent.right = node.left
                # if parent is None, update root node to be left node
                else:
                    self.root = node.left
                
                node.left.parent = parent
                del node
            
            # removing node with two children
            else:
                print('Removing node with two children...')
                
                # find
                predecessor = self.get_predecessor(node.left)
                
                # swapping the root with largest left subtree Node
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                
                # remove
                self.removeNode(data, predecessor) 
    
    # getting the right most item = max
    def get_predecessor(self, node):
        if node.right is not None:
            return self.get_predecessor(node.right)          
        return node
    
    def remove(self, data):
        if self.root is not None:
            self.removeNode(data, self.root)
    
    def traverse(self):
        
        if self.root is not None:
            self.traverseInOrder(self.root)
    
    def getMax(self):
        
        if self.root:
            return self.get_max(self.root)
        
    # finds the right most item   
    def get_max(self, node):
        
        if node.right:
            return self.get_max(node.right)

        return node.data

    def getMin(self):
        
        if self.root:
            return self.get_min(self.root)
    
    # get the left most item
    def get_min(self, node):
        
        if node.left:
            return self.get_min(node.left)
        return node.data
    
        
    # In order, goes from left subtree to root to right subtree (recursion)
    def traverseInOrder(self, node):
        
        # left subtree
        if node.left is not None:
            self.traverseInOrder(node.left)
        
        # root node
        print('%s' % node.data)
        
        # right subtree
        if node.right is not None:
            self.traverseInOrder(node.right)
         
    
bst = BinarySearchTree()

bst.insert(20)
bst.insert(12)
bst.insert(14)
bst.insert(9)
bst.insert(-2)
bst.insert(-5)
bst.insert(100)

bst.remove(-2)
print('Max Right: %s' % bst.get_max(bst.root))
print('Max Left: %s' % bst.get_min(bst.root))

bst.traverse()   
            
            
            