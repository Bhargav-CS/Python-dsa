class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
        s1 = s1 + s1
        
        if s2 in s1:
            return True
        
        else:
            return False
    
s1 = "abcd"
s2 = "cdab"

sol = Solution()
print(sol.areRotations(s1, s2))