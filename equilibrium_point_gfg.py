class Solution:
    #Function to find equilibrium point in the array.
     def findEquilibrium(self, arr):
        # code here
        n = len(arr)
        l,r = 0,sum(arr)-arr[0]
        
        for i in range(1, n-1):
            l += arr[i-1]
            r -= arr[i]
            
            if(l == r):
                return i
                
        return -1
    
arr = [1, 2, 0, 3]
sol = Solution()
print(sol.findEquilibrium(arr))