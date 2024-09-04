class Solution:    
    def nthStair(self, n):
        return n // 2 + 1

n = 2
sol = Solution()
print(sol.nthStair(n))