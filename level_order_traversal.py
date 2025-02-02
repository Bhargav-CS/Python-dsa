from collections import deque

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        d=deque()
        d.append(root)
        ans=[]
        
        while d:
            levelSize=len(d)
            temp=[]
            
            for i in range(levelSize):
                node=d.popleft()
                temp.append(node.data)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
                
            ans.append(temp)
        
        return ans