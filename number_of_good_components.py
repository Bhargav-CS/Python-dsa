
from typing import List


class Solution:
        # code here
        def findNumberOfGoodComponent(self, e: int, v: int, edges: List[List[int]]) -> int:
            def dfs(node):
                visited[node] = True
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        dfs(neighbor)
            
            graph = [[] for _ in range(v + 1)]
            visited = [False] * (v + 1)
            
            for edge in edges:
                u, v = edge
                graph[u].append(v)
                graph[v].append(u)
            
            count = 0
            for node in range(1, v + 1):
                if not visited[node]:
                    dfs(node)
                    count += 1
            
            return count
        
    
    
e = 5
v = 7

edges = [[1, 2], [7, 2], [3, 5], [3, 4], [4, 5]]
sol = Solution()
print(sol.findNumberOfGoodComponent(e, v, edges)) #2