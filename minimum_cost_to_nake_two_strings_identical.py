class Solution:
    def findMinCost(self, x, y, costX, costY):
        # code here
        m, n = len(x), len(y)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + costX
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] + costY
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + costX, dp[i][j-1] + costY)
        return dp[m][n]
    
x = "abcd"
y = "acdb"
costX = 10
costY = 20

sol = Solution()
print(sol.findMinCost(x, y, costX, costY)) # 30