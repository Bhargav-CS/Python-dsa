class Solution:
    
    def maxSubArraySum(self, arr):
        
        maxi = float('-inf')
        sum = 0
        
        for i in range(len(arr)):
            sum += arr[i]
            maxi = max(sum, maxi)
            if sum < 0:
                sum = 0
                
        return maxi
            
# arr = [1, 2, 3, -2, 5]
# arr = [-1, -2, -3, -4]
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
sol = Solution()
print(sol.maxSubArraySum(arr))