class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        tmp = s.split()
        if len(pattern) != len(tmp):
            return False
        d = {}
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != tmp[i]:
                    return False
            else:
                if tmp[i] in d.values():
                    return False
                d[pattern[i]] = tmp[i]
        return True
    
# Example    
pattern = "abba"
s = "dog cat cat dog"

sol = Solution()
print(sol.wordPattern(pattern, s)) # True  