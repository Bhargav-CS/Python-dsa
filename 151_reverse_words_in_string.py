class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        s = list(filter(lambda x: x != "", s))
        s = s[::-1]
        return " ".join(s)
    

s = "the sky is blue"
sol = Solution()
print(sol.reverseWords(s)) # output : "blue is sky the"

