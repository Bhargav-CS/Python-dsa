import sys
sys.setrecursionlimit(10000)

class Solution:
    def cut(self, n, x, y, z, dp):
        # base case
        if n < 0:
            return float('-inf')
        elif n == 0:
            return 0
        # recursive case
        elif dp[n] != -1:
            return dp[n]
        
        cutx = self.cut(n - x, x, y, z, dp)
        cuty = self.cut(n - y, x, y, z, dp)
        cutz = self.cut(n - z, x, y, z, dp)
        
        dp[n] = 1 + max(cutx, cuty, cutz)
        return dp[n]
    
    def maximizeTheCuts(self, n, x, y, z):
        dp = [-1] * (n + 1)
        result = self.cut(n, x, y, z, dp)
        return max(0, result)

# Example usage
n = 4000
x = 1
y = 2
z = 3

sol = Solution()
print(sol.maximizeTheCuts(n, x, y, z))