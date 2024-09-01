class Solution:
    
    def maxPathSum(self, arr1:list[int], arr2:list[int]):
        n = len(arr1)
        m = len(arr2)
        
        i = 0
        j = 0
        sum1 = 0
        sum2 = 0
        ans = 0
        
        while i < n and j < m :
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            
            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]
                j += 1
                
            else:
                ans += max(sum1, sum2) + arr1[i]
                sum1 = 0
                sum2 = 0
                i += 1
                j += 1
                
        while i < n:
            sum1 += arr1[i]
            i += 1
        
        while j < m:
            sum2 += arr2[j]
            j += 1
            
        return ans + max(sum1, sum2)
        
    
    
arr1 = [2, 3, 7, 10, 12] 
arr2 = [1, 5, 7, 8]

sol = Solution()
print(sol.maxPathSum(arr1, arr2))