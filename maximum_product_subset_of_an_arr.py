
class Solution:
    def findMaxProduct(self, arr:list):
        mod = (10**9)+7
        neg = 0
        ans = 1
        arr.sort()
        for i in range(len(arr)):
            if arr[i] < 0:
                neg += 1
        for i in range(len(arr)):
            if arr[i] > 0:
                ans = (ans * arr[i]) % mod
        if neg%2==1:
            neg -=1
        for i in range(neg):
            ans =(ans * arr[i])%mod
        
        return ans
                        
        
        
        
                
# arr = [-1, 0, -2, 4, 3]
# arr = [-1, 0, -2, -4]
arr = [3, -1, 4, -2, 0, -3, 5]
sol = Solution()
print(sol.findMaxProduct(arr))


