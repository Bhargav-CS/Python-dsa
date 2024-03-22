class Solution:
    def lastIndex(self, s):
        return s.rfind('1')
    
s = "00001"
sol = Solution()
print(sol.lastIndex(s)) # 2
