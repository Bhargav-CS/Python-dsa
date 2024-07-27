class Solution:
    def countMin(self, str):
        n = len(str)
        # Create a table to store results of sub-problems
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # Fill the table
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                if str[i] == str[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1
        
        return dp[0][n - 1]
            
                
# str = 'abcd'
# str = 'abccbaabc' #3
# str = 'aa'
str = 'dmtjtvqyiedezraoqkfu' #15
sol = Solution()
print(sol.countMin(str))
