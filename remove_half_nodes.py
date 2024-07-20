from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def buildTree(s):
    if len(s) == 0 or s[0] == "N":
        return None
    
    ip = s.split()
    root = Node(int(ip[0]))
    
    queue = []
    queue.append(root)
    
    i = 1
    
    while len(queue) > 0  and i < len(ip):
        currNode = queue.pop(0)
        currVal = ip[i]
        
        if currVal != "N":
            currNode.left = Node(int(currVal))
            queue.append(currNode.left)
            
        i += 1
        if i >= len(ip):
            break
        
        currVal = ip[i]
        
        if currVal != "N":
            currNode.right = Node(int(currVal))
            queue.append(currNode.right)
            
        i += 1
        
    return root

def printInorder(root):
    if root is None:
        return
    
    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)

class Solution:
    def RemoveHalfNodes(self, node):
        if node is None:
            return 
        
        node.left = self.RemoveHalfNodes(node.left)
        node.right = self.RemoveHalfNodes(node.right)
        
        if node.left is None and node.right is None:
            return node
        
        if node.left is None:
            new_node = node.right
            del node
            return new_node
        
        if node.right is None:
            new_node = node.left
            del node
            return new_node
        
        return node
        
    def levelOrder(self, root):
        if root is None:
            return []
        
        q = deque()
        q.append(root)
        res = []
        
        while q:
            size = len(q)
            
            for i in range(size):
                curr = q.popleft()
                res.append(curr.data)
                
                if curr.left:
                    q.append(curr.left)
                    
                if curr.right:
                    q.append(curr.right)
              
        return res
        
    
s = "5 7 8 2"
root = buildTree(s)
sol = Solution()
fresh = sol.RemoveHalfNodes(root)
printInorder(fresh)   

 
    
