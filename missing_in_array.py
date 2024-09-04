class Solution:
    
    def missingNumber(self, n, arr):
        
        arr = set(arr)
        
        for i in range(1, n+1):
            if i not in arr:
                return i
                
            
            
n = 5
arr = [1, 2, 3, 5]

# n = 2
# arr = [1]

sol = Solution()
print(sol.missingNumber(n, arr))