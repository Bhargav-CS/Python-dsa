class Solution:
    def swapNibbles (self, n):
        # code here 
        n = bin(n)[2:].zfill(8)
        x = n[:(len(n)//2)]
        y = n[len(n)//2:]
        
        return(int(y+x, 2))
    
n = 100
sol = Solution()
print(sol.swapNibbles(n))
