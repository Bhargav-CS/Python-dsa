class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        left = 0
        right = 0
        ans = ""
        
        while right < n:
                if left<0:
                    left = 0
                
                
                if s[left] == s[right]:
                    curr = s[left:right+1]
                    if len(curr) > len(ans) and curr == curr[::-1]:
                        ans = curr
                    print(ans, "left and right matches", "left:",s[left],"right:",s[right])
                    right = right + 1
                    left = left - 1
                    
                    
                elif s[right] == ans :
                    curr = ans + s[right]
                    if len(curr) > len(ans) and curr == curr[::-1]:
                        ans = curr
                    print(ans, "ans matches to right")
                    right = right + 1
                
                else:
                    left = right
                
        
        return ans
    
# s = "babad"
# s = "cbbd"
# s = "aacabdkacaa"
s = "abcda"
sol = Solution()
print(sol.longestPalindrome(s))
