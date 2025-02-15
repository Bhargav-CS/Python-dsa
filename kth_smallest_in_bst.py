def __init__(self):
    self.k=None

def solve(self,root):
    if root:
        l=self.solve(root.left)
        if l!=-1:
            return l
        if self.k==1:
            return root.data
        self.k-=1
        r=self.solve(root.right)
        if r!=-1:
            return r
    return -1

def kthSmallest(self, root, k): 
    self.k=k
    return self.solve(root)