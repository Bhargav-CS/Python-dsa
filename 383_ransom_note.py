class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
            
        ransomNote = list(ransomNote)
        magazine = list(magazine)
            
        for i in ransomNote:
            if i in magazine:
                magazine.remove(i)
            else:
                return False
        return True
    

ransomNote = "a" 
magazine = "b"

sol = Solution()
print(sol.canConstruct(ransomNote, magazine))


        