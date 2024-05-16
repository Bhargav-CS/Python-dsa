class Solution:
    
    #Function to check if two strings are rotations of each other or not.
        def areRotations(self, s1, s2):
            if len(s1) != len(s2):
                return False
            temp = s1 + s1
            if s2 in temp:
                return True
            else:
                return False
    
s1 = "geeksforgeeks"
s2 = "forgeeksgeeks"
sol = Solution()
print(sol.areRotations(s1, s2)) #1
