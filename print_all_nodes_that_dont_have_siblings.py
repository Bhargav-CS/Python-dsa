'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def noSibling(root):
    # code here
    res = []
    def helper(root):
        if not root:
            return
        if not root.left and root.right:
            res.append(root.right.data)
        if not root.right and root.left:
            res.append(root.left.data)
        helper(root.left)
        helper(root.right)
    helper(root)
    if not res:
        return [-1]
    return sorted(res)



