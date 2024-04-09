class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here
        return '.'.join(S.split('.')[::-1])

S = "i.like.this.program.very.much"
sol = Solution()
print(sol.reverseWords(S)) # much.very.program.this.like.i