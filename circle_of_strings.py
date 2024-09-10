from typing import List
from collections import defaultdict, deque

class Solution:
    def isCircle(self, arr: List[str]) -> bool:
        n = len(arr)
        vis = [0] * n
        indegree = [0] * 26
        outdegree = [0] * 26
        mm = defaultdict(list)
        
        for i in range(n):
            indegree[ord(arr[i][0]) - ord('a')] += 1
            outdegree[ord(arr[i][-1]) - ord('a')] += 1
            mm[arr[i][0]].append(i)
        
        for char in mm:
            if indegree[ord(char) - ord('a')] != outdegree[ord(char) - ord('a')]:
                return False
        
        q = deque([0])
        vis[0] = 1
        ans = 1
        
        while q:
            index = q.popleft()
            for x in mm[arr[index][-1]]:
                if not vis[x]:
                    ans += 1
                    vis[x] = 1
                    q.append(x)
        
        if ans == n:
            return 1
        
        else:
            return 0

# Example usage
arr = ["for", "geek", "rig", "kaf"]
sol = Solution()
print(sol.isCircle(arr))  # Expected output: True