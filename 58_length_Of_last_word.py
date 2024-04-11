class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        l = s.split(" ")
        print(l)
        return (len(l[-1]))

s = "   fly me   to   the moon  "
sol  = Solution()
print(sol.lengthOfLastWord(s))

