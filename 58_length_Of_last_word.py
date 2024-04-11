class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])

s = "   fly me   to   the moon  "
sol  = Solution()
print(sol.lengthOfLastWord(s))

