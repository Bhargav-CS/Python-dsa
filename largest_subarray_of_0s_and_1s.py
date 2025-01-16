class Solution:
    def maxLen(self, arr):
        preSum={0:-1}
        currSum=0
        ans=0
        for i in range(len(arr)):
            currSum+= (1 if arr[i] else -1)
            if currSum in preSum:
                ans=max(ans,i-preSum[currSum])
            if currSum not in preSum:
                preSum[currSum]=i
        return ans

# arr = [0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
arr = [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
sol = Solution()
print(sol.maxLen(arr))