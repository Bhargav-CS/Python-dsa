from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
def buildTree(s):
    
    if (len(s) == 0 or s[0] == "N"):
        return None
    
    ip = list(map(str, s.split()))
    
    root = Node(int(ip[0]))
    size = 0
    q = deque()
    
    q.append(root)
    
    size += 1
    
    i = 1
    
    while (size > 0 and i < len(ip)):
        currNode = q[0]
        q.popleft()
        size = size - 1
        
        currVal = ip[i]
        
        if (currVal != "N"):
            currNode.left = Node(int(currVal))
            
            q.append(currNode.left)
            size += 1
            
        i += 1
        
        if (i>= len(ip)):
            break
        
        currVal = ip[i]
        
        
        if (currVal != "N"):
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
            
            size = size + 1
            
        i = i + 1
        
    return root
        
    
        
class Solution:
    def inOrder(self, root):
        if not root:
            return []
        
        return self.inOrder(root.left) + [root.data] + self.inOrder(root.right)
        

s = "1 2 3 4 5"
root = buildTree(s)
sol = Solution()
res = sol.inOrder(root)

print(res)