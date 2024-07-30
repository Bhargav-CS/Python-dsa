from typing import List

class Solution:
	def __init__(self):
		self.ans = []

	def solve(self, i: int, j: int, n: int, m: int, s: str, vis: List[List[int]], mat: List[List[int]]):
		# base case
		if i < 0 or j < 0 or i >= n or j >= m or vis[i][j] or mat[i][j] == 0:
			return
		if i == n - 1 and j == m - 1:
			self.ans.append(s)
			return
		# recursive case
		vis[i][j] = 1
		self.solve(i + 1, j, n, m, s + 'D', vis, mat)
		self.solve(i, j + 1, n, m, s + 'R', vis, mat)
		self.solve(i - 1, j, n, m, s + 'U', vis, mat)
		self.solve(i, j - 1, n, m, s + 'L', vis, mat)
		vis[i][j] = 0
		return

	def findPath(self, mat: List[List[int]]) -> List[str]:
		# codeGenius
		n = len(mat)
		m = len(mat[0])
		if mat[0][0] == 0:
			return ["-1"]
		vis = [[0 for _ in range(m)] for _ in range(n)]
		self.solve(0, 0, n, m, "", vis, mat)
		return self.ans

# Example usage
m = [[1, 0, 0, 0],
	 [1, 1, 0, 1], 
	 [1, 1, 0, 0],
	 [0, 1, 1, 1]]

sol = Solution()
print(sol.findPath(m))