def solve(self,root,ans):
    if root:
        l=self.solve(root.left,ans)
        r=self.solve(root.right,ans)
        ans[0]=max(ans[0],l+r)
        return 1+max(l,r)
    return 0

def diameter(self, root):
    ans=[0]
    self.solve(root,ans)
    return ans[0]