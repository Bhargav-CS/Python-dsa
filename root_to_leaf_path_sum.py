from collections import deque

class Node:
    def __init__(self, val):
        self.left = None
        self.data = val
        self.right = None
        
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

    while (size > 0 and i < len(ip)):
        currNode = q[0]
        q.popleft()
        size = size - 1
        
        currVal = ip[i]
        
        if currVal != "N":
            currNode.left = Node(int(currVal))
            q.append(currNode.left)
            size = size + 1
        
        i = i + 1
        if i >= len(ip):
            break
        
        currVal = ip[i]
        
        if currVal != "N":
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
            size = size + 1
        i = i + 1
        
    return root
            
class Solution:
                
    def hasPathSum(self, root, target):
        if root is None:
            return False
        
        q = deque()
        q.append(root)
        # res = [root.data]
        ass = deque()
        ass.append(root.data)
        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                sum = ass.popleft()
                # print(f"in the {i} iteration value of curr", curr.data, "level", level, "res", res)
                if curr.left:
                    q.append(curr.left)
                    # res.append(curr.left.data + sum)
                    ass.append(curr.left.data + sum)
                    
                if curr.right:
                    q.append(curr.right)
                    # res.append(curr.right.data + sum)
                    ass.append(curr.right.data + sum)
                    
                if not curr.left and not curr.right:
                    if sum == target:
                        return True
        
        return False
        
        
    
    def preorder(self, root, a=[]):
        '''Root -> Left -> Right'''
        if root is None:
            return
        a.append(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
        
        return a
    
    def inorder(self, root, a=[]):
        '''Left -> Root -> Right'''
        if root is None:
            return
        self.inorder(root.left)
        a.append(root.data)
        self.inorder(root.right)
        
        return a
            
    def postorder(self, root):
        '''Left -> Right -> Root'''
        if root is None:
            return
        
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)
        
        
# s = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
s = '1 2 3 4 5 6 7'
# s = '1 2 3 4 N 5 N'
sum = 7
root = buildTree(s)
sol = Solution()
print(sol.hasPathSum(root, sum))

