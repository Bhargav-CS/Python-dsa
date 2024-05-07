'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def reverseLevelOrder(root):
    # code here
    res = []
    def helper(root):
        if not root:
            return
        q = []
        q.append(root)
        while q:
            temp = q.pop(0)
            res.append(temp.data)
            if temp.right:
                q.append(temp.right)
            if temp.left:
                q.append(temp.left)
    helper(root)    
    return res[::-1]

