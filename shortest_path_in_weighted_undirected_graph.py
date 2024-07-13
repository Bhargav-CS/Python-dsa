
    
from typing import List
from collections import deque

class Solution:

    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        dp = [[float('inf'), -1] for _ in range(n + 1)]
        ans = []
        pq = deque()
        adj = [[] for _ in range(n + 1)]
        dp[1][0] = 0

        for edge in edges:
            adj[edge[0]].append((edge[1], edge[2]))
            adj[edge[1]].append((edge[0], edge[2]))

        pq.append(1)
        while pq:
            x = pq.popleft()
            for itr in adj[x]:
                if dp[x][0] + itr[1] < dp[itr[0]][0]:
                    dp[itr[0]][0] = dp[x][0] + itr[1]
                    dp[itr[0]][1] = x
                    pq.append(itr[0])

        if dp[n][1] == -1:
            return [-1]

        ans.append(dp[n][0])
        i = n
        while i >= 1:
            ans.append(i)
            i = dp[i][1]

        ans[1:] = reversed(ans[1:])

        return ans

n = 5
m  = 6
edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
sol = Solution()
print(sol.shortestPath(n, m, edges))