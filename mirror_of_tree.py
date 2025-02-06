class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Code here
        if not root or (not root.left and not root.right): return 
        root.left,root.right=root.right,root.left
        self.mirror(root.left)
        self.mirror(root.right)