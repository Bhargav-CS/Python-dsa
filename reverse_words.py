class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,str):
        # code here 
        return '.'.join(str.split('.')[::-1])
    
    
str = "i.like.this.program.very.much"
sol = Solution()
print(sol.reverseWords(str))