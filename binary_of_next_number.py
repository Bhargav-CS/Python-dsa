class Solution:
    def binaryNextNumber(self, s):
        s = int(s, 2) + 1
        return bin(s)[2:]
    
s = '10'
sol = Solution()
print(sol.binaryNextNumber(s))