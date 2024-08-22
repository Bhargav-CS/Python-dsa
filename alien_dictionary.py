from typing import List
from collections import deque, defaultdict

class Solution:
    def findOrder(self, alien_dict: List[str], N: int, K: int) -> str:
        # Create adjacency list and in-degree array
        adj = defaultdict(list)
        indeg = [0] * K
        
        # Build the graph
        for i in range(N - 1):
            s1 = alien_dict[i]
            s2 = alien_dict[i + 1]
            len_min = min(len(s1), len(s2))
            for j in range(len_min):
                if s1[j] != s2[j]:
                    adj[ord(s1[j]) - ord('a')].append(ord(s2[j]) - ord('a'))
                    indeg[ord(s2[j]) - ord('a')] += 1
                    break
        
        # Perform topological sort using BFS
        q = deque()
        for i in range(K):
            if indeg[i] == 0:
                q.append(i)
        
        ans = []
        while q:
            node = q.popleft()
            ans.append(chr(node + ord('a')))
            for neighbor in adj[node]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    q.append(neighbor)
        
        return ''.join(ans)

# Example usage
N = 3
K = 3
alien_dict = ["caa", "aaa", "aab"]

sol = Solution()
print(sol.findOrder(alien_dict, N, K))  # Expected output: "cab"