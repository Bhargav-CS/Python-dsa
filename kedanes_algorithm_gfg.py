#User function Template for python3

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