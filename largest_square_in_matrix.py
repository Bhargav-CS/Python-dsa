from typing import List

class Solution:
    def maxSquare(self, n: int, m: int, mat: List[List[int]]) -> int:
        dp = [[0] * m for _ in range(n)]  # Initialize a matrix to store the lengths of squares
        ans = 0

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = mat[i][j]  # For the first row and column, the length is the same as the input matrix
                elif mat[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1  # Calculate the length of the square

                ans = max(ans, dp[i][j])  # Update the maximum square length

        return ans


n = 6
m = 5
mat = [[0, 1, 1, 0, 1], 
       [1, 1, 0, 1, 0],
       [0, 1, 1, 1, 0],
       [1, 1, 1, 1, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0]]

sol = Solution()
print(sol.maxSquare(n, m, mat))
