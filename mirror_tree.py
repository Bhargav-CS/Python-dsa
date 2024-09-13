from collections import deque

class Node:
    
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
def inorderTraversalUtil(root):
    
    if root is None:
        return
    
    inorderTraversalUtil(root.left)
    print(root.data, end=" ")
    inorderTraversalUtil(root.right)
    
def inorderTraversal(root):
    inorderTraversalUtil(root)
    print()
    
def buildTree(s):
    
    if (len(s) == 0 or s[0] == "N"):
        return None
    
    ip = list(map(str, s.split()))
    
    root = Node(int(ip[0]))
    size = 0
    q = deque()
    
    q.append(root)
    size = size + 1
    
    i = 1
    
    while size > 0 and i< len(ip):
        
        currNode = q[0]
        q.popleft()
        size = size - 1
        
        currVal = ip[i]
        
        if(currVal != "N"):
            currNode.left = Node(int(currVal))
            q.append(currNode.left)
            size += 1
            
        i += 1
        
        if i>= len(ip):
            break
        currVal = ip[i]
        
        if currVal!="N":
            
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
            size += 1
        
        i += 1
        
    return root


class Solution:
    def mirror(self, root):
        dq = deque()
        dq.append(root)
        
        while dq:
            node = dq.popleft()
            
            if node.left:
                dq.append(node.left)
                
            if node.right:
                dq.append(node.right)
            
            node = self.helper(node)
        
        return root
            
            
    
    def helper(self, node):
        
        if node is None:
            return 
        
        node.left, node.right = node.right, node.left
        return node

# s = "10 20 30 40 60 N N"
s = "1 2 3"
root = buildTree(s)
sol = Solution()
sol.mirror(root)
inorderTraversal(root)