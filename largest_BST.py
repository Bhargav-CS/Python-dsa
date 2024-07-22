class Solution:
    def largestBst(self, root):
        # Your code here
        if not root:
            return 0
        self.ans = 0
        self.helper(root)
        return self.ans
    
    def helper(self, root):
        if not root:
            return (True, 0, float('inf'), float('-inf'))
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if left[0] and right[0] and left[3] < root.data < right[2]:
            size = left[1] + right[1] + 1
            self.ans = max(self.ans, size)
            return (True, size, min(left[2], root.data), max(right[3], root.data))
        return (False, max(left[1], right[1]), 0, 0)
    
    
    
