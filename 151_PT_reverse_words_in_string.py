class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1]).strip()
    
s = "the sky is blue"
s = "  hello world  "
sol = Solution()
print(sol.reverseWords(s))