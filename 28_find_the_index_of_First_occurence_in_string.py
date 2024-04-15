class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

haystack = "sadbutsad"
needle = "sad"
sol = Solution()
print(sol.strStr(haystack, needle))
