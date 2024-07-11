
from typing import List, Set

class Solution:
    def dfs(self, grid: List[List[int]], i: int, j: int, index: int) -> int:
        # Base case
        n = len(grid)
        if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
            return 0
        # Recursive case
        grid[i][j] = index
        count = (self.dfs(grid, i + 1, j, index) + self.dfs(grid, i - 1, j, index) +
                 self.dfs(grid, i, j - 1, index) + self.dfs(grid, i, j + 1, index))
        return count + 1

    def neighbours(self, grid: List[List[int]], i: int, j: int, s: Set[int]):
        n = len(grid)
        if i > 0:
            s.add(grid[i - 1][j])
        if j > 0:
            s.add(grid[i][j - 1])
        if i < n - 1:
            s.add(grid[i + 1][j])
        if j < n - 1:
            s.add(grid[i][j + 1])

    def MaxConnection(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        index = 2
        mp = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    mp[index] = self.dfs(grid, i, j, index)
                    res = max(res, mp[index])
                    index += 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    s = set()
                    self.neighbours(grid, i, j, s)
                    count = 1
                    for idx in s:
                        count += mp.get(idx, 0)
                    res = max(res, count)
        return res

grid = [[1, 0, 1],
        [1, 0, 1],
        [1, 0, 1]]

sol = Solution()
print(sol.MaxConnection(grid))