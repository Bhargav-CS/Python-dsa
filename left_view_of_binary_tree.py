from collections import deque


class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.left = None
        self.right = None
        
        
def buildTree(s):
    
    if len(s) == 0 or s[0] == "N":
        return None
    
    ip = list(map(str, s.split()))
    
    root = Node(int(ip[0]))
    
    size = 0
    q = deque()
    
    q.append(root)
    size += 1
    
    i = 1
    
    while(size > 0 and i < len(ip)):
        currNode = q[0]
        q.popleft()
        size = size - 1
        
        currVal = ip[i]
        
        if currVal != "N":
            
            currNode.left = Node(int(currVal))
            
            q.append(currNode.left)
            size = size + 1
            
        i = i + 1
        
        if(i>=len(ip)):
            break
        
        currVal = ip[i]
        
        if currVal != "N":
            
            currNode.right = Node(int(currVal))
            
            q.append(currNode.right)
            size = size + 1
            
        i = i + 1
        
    return root


def leftView(root):
    
    if root is None:
        return
    
    q = deque()
    q.append(root)
    res = []
    
    while q:
        size = len(q)
        level = []
        
        for i in range(size):
            curr = q.popleft()
            level.append(curr.data)
            
            if curr.left:
                q.append(curr.left)
                
            if curr.right:
                q.append(curr.right)
                
        res.append(level)
        
    for row in res:
        print(row[0], end=" ")
        
    return ""
        
    
    
    

s = "1 2 3 4 5 6 7 N 8 N N N N N N"
root = buildTree(s)

print(leftView(root))


