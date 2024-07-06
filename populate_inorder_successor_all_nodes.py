class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None
        
class Solution:
    def populateNext(self, root):
        def inorder(node, prev):
            if node:
                prev = inorder(node.left, prev)
                if prev:
                    prev.next = node
                prev = node
                prev = inorder(node.right, prev)
            return prev
        
        inorder(root, None)
        return root
    
    