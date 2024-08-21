from collections import deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        # Create an adjacency list of size n for storing the undirected graph.
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        # A dist array of size n initialized with a large number to 
        # indicate that initially all the nodes are untraversed.
        dist = [float('inf')] * n
        dist[src] = 0
        
        # BFS Implementation.
        q = deque([src])
        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if dist[node] + 1 < dist[neighbor]:
                    dist[neighbor] = dist[node] + 1
                    q.append(neighbor)
        
        # Updated shortest distances are stored in the resultant array `ans`.
        # Unreachable nodes are marked as -1.
        ans = [-1 if d == float('inf') else d for d in dist]
        return ans


n = 9
m = 10
edges = [[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]]
src = 0
sol = Solution()
ans = sol.shortestPath(edges, n, m, src)
print(" ".join(map(str, ans)))