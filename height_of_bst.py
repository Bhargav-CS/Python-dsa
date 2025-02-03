class Solution:
    #Function to find the height of a binary tree.
    def height(self, node):
        
        if node is None:
            return -1
        else:
            return max(self.height(node.left),self.height(node.right)) +1