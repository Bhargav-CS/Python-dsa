def solve(self,root,ans):
    if root:
        l=max(0,self.solve(root.left,ans))
        r=max(0,self.solve(root.right,ans))
        ans[0]=max(ans[0],l+r+root.data)
        return root.data+max(l,r)
    return 0

def findMaxSum(self, root): 
    ans=[-float("inf")]
    self.solve(root,ans)
    return ans[0]