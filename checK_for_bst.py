class Solution:
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        def isBSTUtil(root, mini, maxi):
            if root is None:
                return True
            if root.data < mini or root.data > maxi:
                return False
            return isBSTUtil(root.left, mini, root.data - 1) and isBSTUtil(root.right, root.data + 1, maxi)
        return isBSTUtil(root, float('-inf'), float('inf'))
    
    
        