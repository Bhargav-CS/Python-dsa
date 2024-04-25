class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = 0
        res = 0
        char_index = {}
        for i in range(len(s)):
            if s[i] in char_index:
                left = max(left, char_index[s[i]] + 1)
    
            res = max(res, i - left + 1)
            char_index[s[i]] = i
        return res


s = "abcabcbb"
sol = Solution()
print(sol.lengthOfLongestSubstring(s)) # 3