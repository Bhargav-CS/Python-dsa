class Solution:
    def addBinary(self,s1, s2):
        return bin(int(s1, 2) + int(s2, 2)).replace("0b", "").lstrip("0")
        
    
    
# s1 = "1101"
# s2 = "111"

s1 = "00100"
s2 = "010"

sol = Solution()
print(sol.addBinary(s1, s2))