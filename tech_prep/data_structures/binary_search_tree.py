class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.next = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        '''Insert value into BST.'''
        if not self.root:
            self.root = TreeNode(value)
            return
        
        curr = self.root
        while True:
            if value < curr.value:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(value)
                    return
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right= TreeNode(value)
                    return