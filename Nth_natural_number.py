class Solution:
    def findNth(self,n):
        ans,place=0,1
        while n:
            ans+=place*(n%9)
            n//=9
            place*=10
        return ans
        
        
    
        
    
n = 9
sol = Solution()
print(sol.findNth(n))