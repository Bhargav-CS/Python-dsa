class Solution:
    def kPangram(self, string:str, k:int):
        #2847
        
        string = string.replace(" ", "")
        if len(string) < 26:
            return False, "length is less than 26"
        
        # alphaSet = set("abcdefghijklmnopqrstuvwxyz")
        string = set(string)
        
        
        if len(string) == 26:
            return True
        
        if len(string) + k >= 26:
            return True
        
        else:
            return False
        
        
        
    
# str = "the quick brown fox jumps over the lazy dog"
str = "aaaaaaaaaaaaaaaaaaaaaaaaaa"
str = "a b c d e f g h i j k l m"
k = 20
sol = Solution()
print(sol.kPangram(str, k))
