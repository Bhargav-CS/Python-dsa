class Solution:
    def nthCharacter(self, s, r, n):
        for _ in range(r):
            s = s.replace('0', '01').replace('1', '10')
        return s[n]
        
s = "1010"
r = 1
n = 2    
sol = Solution()
print(sol.nthCharacter(s, r, n)) # 0
