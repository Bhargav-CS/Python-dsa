    
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
def new_node(val):
    return Node(val)

def build_tree(s):
    if not s or s[0] == "N":
        return None
    
    ip = s.split()
    
    root = new_node(int(ip[0]))
    
    queue = []
    queue.append(root)
    
    i = 1
    
    while queue and i < len(ip):
        
        currNode = queue.pop(0)
        currVal = ip[i]
        
        if currVal != "N":
            currNode.left = new_node(int(currVal))
            queue.append(currNode.left)
            
        i += 1
        if i > len(ip):
            break
        currVal = ip[i]
        
        if currVal != "N":
            currNode.right = new_node(int(currVal))
            queue.append(currNode.right)
            
        i += 1
        
    return root

        

class Solution:
    def traverse(self, root):
        if root is None:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        return root.data + left + right

    def is_sum_tree(self, root):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is not None or root.right is not None:
            if root.data != self.traverse(root.left) + self.traverse(root.right):
                return False
        return self.is_sum_tree(root.left) and self.is_sum_tree(root.right)


           
        
# s = "3 1 2"
# s = "10 20 30 10 10"
s = "5 1 4"
root = build_tree(s)
sol = Solution()
print(sol.is_sum_tree(root))
# print(sol.preoder(root))