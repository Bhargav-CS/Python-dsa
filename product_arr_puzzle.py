class Solution:
    def productExceptSelf(self, arr):
        #code here
        n = len(arr)
        l,r = [1]*n,[1]*n
        
        for i in range(1, n):
            l[i] = l[i-1]*arr[i-1]
            
        for i in range(n-2, -1, -1):
            r[i] = r[i+1]*arr[i+1]
            
        for i in range(n):
            arr[i] = l[i]*r[i]
            
        return arr
    
arr = [10, 3, 5, 6, 2]
sol = Solution()
print(sol.productExceptSelf(arr))