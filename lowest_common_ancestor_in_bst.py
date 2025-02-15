class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def LCA(self, root, n1, n2):
        if not root:
            return 
        
        curr=root.data
        
        if n1.data>curr and n2.data>curr:
            return self.LCA(root.right,n1,n2)
        elif n1.data<curr and n2.data<curr:
            return self.LCA(root.left,n1,n2)
        else:
            return root