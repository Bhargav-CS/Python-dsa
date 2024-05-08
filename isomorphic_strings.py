class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        if len(str1) != len(str2):
            return False
        d1 = {}
        d2 = {}
        for i in range(len(str1)):
            if str1[i] in d1:
                if d1[str1[i]] != str2[i]:
                    return False
            else:
                d1[str1[i]] = str2[i]
            if str2[i] in d2:
                if d2[str2[i]] != str1[i]:
                    return False
            else:
                d2[str2[i]] = str1[i]
        return True
    
    
str1 = "aab"
str2 = "xxy"

sol = Solution()
print(sol.areIsomorphic(str1, str2)) # True