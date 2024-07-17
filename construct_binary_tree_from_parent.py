from collections import deque

'''
# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Solution:
    #Function to construct binary tree from parent array.
    def createTree(self,parent):
        # code here
        n = len(parent)
        map = {}
        for i in range(n):
            map[i] = Node(i)
        
        root = None
        
        for i in range(n):
            
            if parent[i] == -1:
                root = map[i]
            else:
                
                if map[parent[i]].left is None:
                    map[parent[i]].left = map[i]
                
                else:
                    map[parent[i]].right = map[i]
        
        return root
    
def preorder(root):
    
    if root:
        print(root.key, end="->")
        preorder(root.left)
        preorder(root.right)
        
def levelorder(root):
    if root is None:
        return []
    
    q = deque()
    q.append(root)
    res = []
    
    while q:
        size = len(q)
        # level = []
        for i in range(size):
            curr = q.popleft()
            res.append(curr.key)
            
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
                
            
        # res.append(level)
        
    return res
    
    
    
    
parent = [-1, 0, 0, 1, 1, 3, 5]
sol = Solution()
root = sol.createTree(parent)

# preorder(root)
# print(levelorder(root))
