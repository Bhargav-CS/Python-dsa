from collections import deque

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
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
        
        if(currVal != "N"):
            
            currNode.left = Node(int(currVal))
            q.append(currNode.left)
            size += 1
            
        i += 1
        
        if(i>=len(ip)):
            break
        
        currVal = ip[i]
        
        if currVal != "N":
            currNode.right = Node(int(currVal))
            
            q.append(currNode.right)
            size += 1
            
        i += 1
    
    return root

def printDLL(head):
    prev = None
    
    while (head != None):
        print(head.data, end = " ")
        prev = head
        head = head.right
    
    print("")
    
    while (prev != None):
        print(prev.data, end = " ")
        prev = prev.left
        
    print("")
    
    
# class Solution:
#     def bToDLL(self, root):
#         ans = self.inorder(root)
#         n = len(ans)
#         head = Node(ans[0])
#         current = head

#         for i in range(1, n):
#             current.right = Node(ans[i])
#             current.right.left = current
#             current = current.right
            
#         return head
    
    
#     def inorder(self, root, ans=[]):
        
#         if root is None:
#             return
        
#         self.inorder(root.left)
#         ans.append(root.data)
#         self.inorder(root.right)
        
#         return ans

class Solution:
    
    def bToDLL(self, root):
        if root is None:
            return None
        
        head, prev = self.bToDLLUtil(root)
        
        return head
    
    def bToDLLUtil(self, root):
        if root is None:
            return None, None
        
        leftHead, leftTail = self.bToDLLUtil(root.left)
        rightHead, rightTail = self.bToDLLUtil(root.right)
        
        if leftTail is not None:
            leftTail.right = root
            root.left = leftTail
            
        else:
            leftHead = root
            
        if rightHead is not None:
            root.right = rightHead
            rightHead.left = root
            
        else:
            rightTail = root
            
        return leftHead, rightTail
        

    
# s = "10 20 30 40 60 N N"
s = "1 3 10 5 7 9 N 5 5 9 2 10"
root = buildTree(s)
sol = Solution()
head = sol.bToDLL(root)
printDLL(head)


