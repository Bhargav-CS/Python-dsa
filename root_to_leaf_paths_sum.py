class Solution:
    def treePathSum(self,root):
        ans=[]
        def solve(root,s):
            if root and root.left==None and root.right==None:
                ans.append(s*10+root.data)
            elif root:
                solve(root.left,s*10+root.data)
                solve(root.right,s*10+root.data)
            else:
                return 0
        solve(root,0)
        return sum(ans)