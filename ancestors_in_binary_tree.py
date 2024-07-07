from collections import deque

class Solution:
    
    def dfs(self, root, target, ans):
        if root:
            if root.data==target:
                return True
            ans.appendleft(root.data)
            if self.dfs(root.left,target,ans):
                return True
            if self.dfs(root.right,target,ans):
                return True
            ans.popleft()
    
    def Ancestors(self, root, target):
        ans=deque()
        self.dfs(root,target,ans)
        return ans