class Node:
    
    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None
    
class DepthFirstSearch:

    # PRE ORDER
    def preOrder(root): 

        if not root:
            return None

        print(root.val)
        preOrder(root.left)
        preOrder(root.right)

    # IN ORDER
    def inOrder(root):

        if not root:
            return None
        
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)



    # POST ORDER
    def postOrder(root):

        if not root:
            return None
        
        postOrder(root.left)
        postOrder(root.right)
        print(root.val)

