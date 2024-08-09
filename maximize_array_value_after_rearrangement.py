class Solution:
    def Maximize(self, a): 
        # Complete the function
        a.sort()
        ans = 0
        
        for i in range(len(a)):
            ans += arr[i] * i
            
        return ans % (10**9 + 7)
            
    
arr = [5, 3, 2, 4, 1]
# arr = [1, 2, 3]
sol = Solution()
print(sol.Maximize(arr))