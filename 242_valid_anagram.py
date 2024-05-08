class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t) != len(s):
            return False
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            if s[i] in d1:
                d1[s[i]] += 1
            else:
                d1[s[i]] = 1
            if t[i] in d2:
                d2[t[i]] += 1
            else:
                d2[t[i]] = 1
        return d1 == d2
    
    
    
s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t)) # True