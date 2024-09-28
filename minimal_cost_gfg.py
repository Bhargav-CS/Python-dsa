class Solution:
    def minimizeCost(self, k, arr):
        n=len(arr)
        dp=[float("inf")]*(n+1)
        dp[1]=0
        for i in range(1,n+1):
            for j in range(1,k+1):
                if n-j>=0:
                    dp[i]=min(dp[i],abs(arr[i-1]-arr[i-1-j])+dp[i-j])
        return dp[n]