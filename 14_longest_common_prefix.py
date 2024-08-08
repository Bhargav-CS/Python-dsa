class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if len(strs) == 0:
            return prefix
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != c:
                    return prefix
            prefix += c
        return prefix
        

strs = ["flower","flow","flight"]
sol = Solution()
print(sol.longestCommonPrefix(strs))    # Output: "fl"

#solving the problem one more time