from collections import deque, defaultdict
import sys
sys.setrecursionlimit(50000)

class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

class Solution:
    def solve(self, root, x, y, mp):
        # base case
        if root is None:
            return
        if x not in mp or mp[x][0] <= y:
            mp[x] = (y, root.data)
        self.solve(root.left, x - 1, y + 1, mp)
        self.solve(root.right, x + 1, y + 1, mp)

    def bottomView(self, root):
        mp = {}
        self.solve(root, 0, 0, mp)
        ans = []
        for key in sorted(mp.keys()):
            ans.append(mp[key][1])
        return ans


    
def buildTree(s):
    
    #First check if we can actually make a tree
    
    if (len(s) == 0 or s[0] == "N"):
        return None
    
    #creating list strings from input string after splitting by space
    ip = list(map(str, s.split()))
    
    #create the root node
    root = Node(int(ip[0]))
    size = 0
    q = deque()
    
    #push the root node into the queue
    q.append(root)
    size += 1
    
    #We can start from the second index since we have already pushed the root node
    i = 1
    
    #While there are elements in the queue and the counter is less than the list of elements
    while(size>0 and i < len(ip)):
        
        #Get and remove the front of the node
        currNode = q[0]
        q.popleft()
        size = size - 1

        #Get the value of the current node from the string
        currVal = ip[i]
        
        #If the left child is not null
        if(currVal != "N"):
            
            #Creating the left child of the tree
            currNode.left = Node(int(currVal))
            
            #Push it to the queue
            q.append(currNode.left)
            size += 1
            
        #For the right child    
        i = i + 1
        if(i>=len(ip)):
            break
        
        currVal = ip[i]
        
        #If the right child is not null
        if(currVal != "N"):
            
            #Create the right child for the current node
            currNode.right = Node(int(currVal))
            
            #Push it to the queue
            q.append(currNode.right)
            size += 1
            
        i = i + 1
    
    return root
            
s = '1 3 2'
root = buildTree(s)
sol = Solution()
print(sol.bottomView(root))