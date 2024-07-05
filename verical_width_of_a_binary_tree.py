
from collections import deque

def verticalWidth(root):
    s = set()
    fillset(root, 0, s)
    return len(s)
    
def fillset(root, hd, s):
    if root is None:
        return
    
    fillset(root.left, hd-1, s)
    s.add(hd)
    fillset(root.right, hd+1, s)

class Node:
    def __init__(self, val):
        self.val = val
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
        size -= 1
        
        currVal = ip[i]
        
        if (currVal != "N"):
            currNode.left = Node(int(currVal))
            q.append(currNode.left)
            size += 1
            
        i += 1
        if (i >= len(ip)):
            break
        
        currVal = ip[i]
        
        if (currVal != "N"):
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
            size += 1
            
        i += 1
        
    return root


    
    