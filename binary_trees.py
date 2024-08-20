from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 
        
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
        
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        
        elif traversal_type == "levelorder":
            return self.leveorder(tree.root)
        
        else:
            print("traversal type is not supported")
            
    def leveorder(self, root):
        '''level by level'''
        if root is None:
            return []
        
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
        
        return res
                    
    def preorder_print(self, start, traversal):
        """Root -> Left -> Right"""
        
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
            
        return traversal
    
    def inorder_print(self, start, traversal):
        """Left -> Root -> Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.data) + "-")
            traversal = self.inorder_print(start.right, traversal)
            
        return traversal
    
    def postorder_print(self, start, traversal):
        """Left -> Right -> Root """
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.data) + "-")
            
        return traversal            
        
        
def buildTree(s):
    #building a tree using a string
    if len(s) == 0 or s[0] == 'N':
        return None
    
    ip = list(map(str, s.split()))
    
    root = Node(int(ip[0]))
    size = 0
    q = deque()
    
    q.append(root)
    size += 1
    
    i = 1
    
    while size > 0 and i < len(ip):
        currNode = q[0]
        q.popleft()
        size -= 1
        
        currVal = ip[i]
        
        if currVal != 'N':
            currNode.left = Node(int(currVal))
            q.append(currNode.left)
            size += 1
            
        i += 1
        if i >= len(ip):
            break
        
        currVal = ip[i]
        
        if currVal != 'N':
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
            size += 1
            
        i += 1
        
    return root


    

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)


# print(tree.print_tree("preorder"))
# print(tree.print_tree("inorder"))
# print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))