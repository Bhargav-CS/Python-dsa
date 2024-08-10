class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
        
    
# s = "anagram"
# t = "nagaram"

s = "aacc"
t = "ccac"

sol = Solution()
print(sol.isAnagram(s, t))