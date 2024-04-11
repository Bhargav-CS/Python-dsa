class Solution:    
    ##Complete this function
    # function to convert a given Gray equivalent n to Binary equivalent.
    def grayToBinary(self,n):
        ans = 0
        while n:
            ans ^= n
            n >>= 1
        return ans
        
        
        

n = 203
sol = Solution()
print(sol.grayToBinary(n)) # ans is 7

