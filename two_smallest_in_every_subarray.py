class Solution:
    def pairWithMaxSum(self, arr):
        
        max1=1
        for i in range(len(arr)-1):
            sum1=arr[i]+arr[i+1]
            max1=max(sum1,max1)
        if max1==1:
            return -1
        return max1
        
        
    
arr = [4, 3, 1, 5, 6]
# arr = [1]
sol = Solution()
print(sol.pairWithMaxSum(arr))